from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from electronics.models import Product, NetworkElectronics
from electronics.validators import NetworkElectronicsValidator


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class NetworkElectronicsSerializer(ModelSerializer):
    # products = ProductSerializer(many=True)
    class Meta:
        model = NetworkElectronics
        fields = "__all__"

    def validate(self, data):
        """Проверяем валидность данных."""
        required_fields = ['level', 'link_type']
        for field in required_fields:
            if field not in data:
                raise ValidationError(f"Поле '{field}' обязательно для заполнения.")

        NetworkElectronicsValidator()(data)
        return data
