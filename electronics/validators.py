from rest_framework.serializers import ValidationError


class NetworkElectronicsValidator:

    def __call__(self, data):
        self.validate_level(data)
        self.validate_factory_levels(data)
        self.validate_supplier(data)
        self.validate_level_factory(data)

    def validate_level(self, data):
        """Уровень может быть равен от 0 до 2."""

        if data.get("level") > 2:
            raise ValidationError("Уровень не может быть больше 2")

    def validate_factory_levels(self, data):
        link_type = data.get("link_type")

        if link_type == "FC":
            if data.get("level") != 0:
                raise ValidationError("Уровень завода всегда должен быть равен 0")

    def validate_supplier(self, data):
        link_type = data.get("link_type")

        if link_type == "FC":
            if data.get("supplier") is not None:
                raise ValidationError("У завода не может быть поставщика электроники")

    def validate_level_factory(self, data):
        link_type = data.get("link_type")
        supplier = data.get("supplier")
        if link_type == "RN" or link_type == "IE":
            if supplier and supplier.link_type == "FC":
                if data.get("level") != 1:
                    raise ValidationError(
                        "Уровень сети должен быть 1, если поставщик — завод"
                    )
