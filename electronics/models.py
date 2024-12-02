from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Создание продукта реализации."""

    title = models.CharField(
        max_length=100,
        verbose_name='Название товара',
        help_text='Введите название товара',
    )
    model = models.CharField(
        max_length=100,
        verbose_name='Модель',
        help_text='Введите модель товара',
        **NULLABLE,
        )
    release_date = models.DateField(
        verbose_name='Дата выпуска',
        help_text='Введите дату выпуска товара',
        **NULLABLE,
    )
    image = models.ImageField(
        verbose_name='Изображение товара',
        help_text='Загрузите изображение товара',
        upload_to='photo/product/',
        **NULLABLE,
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class NetworkElectronics(models.Model):
    """Организация сети по реализации электроники."""

    class Status(models.TextChoices):
        FACTORY = "FC", "Завод"
        RETAIL_NETWORK = "RN", "Розничная сеть"
        INDIVIDUAL_ENTREPRENEUR = "IE", "Индивидуальный предприниматель"


    name = models.CharField(
        max_length=100,
        verbose_name="Название организации",
        help_text="Введите название организации",
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        help_text="Введите адрес электронной почты",
        unique=True,
    )
    country = models.CharField(
        max_length=100,
        verbose_name="Страна",
        help_text="Введите название страны",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        help_text="Введите название города",
        **NULLABLE,
    )
    street = models.CharField(
        max_length=100,
        verbose_name="Улица",
        help_text="Введите название улицы",
        **NULLABLE,
    )
    house_number = models.CharField(
        max_length=10,
        verbose_name="Номер дома",
        help_text="Введите номер дома",
        **NULLABLE,
    )
    link_type = models.CharField(
        max_length=100,
        choices=Status.choices,
        verbose_name="Тип организации",
        help_text="Выберите тип организации",
    )
    supplier = models.ForeignKey(
    'self',
        default=None,
        on_delete=models.SET_DEFAULT,
        verbose_name='Поставщик',
        help_text='Укажите поставщика',
        **NULLABLE,
    )
    duty = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Задолженность перед поставщиком",
        help_text="Введите задолженность перед поставщиком",
        **NULLABLE,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания записи",
        help_text="Дата создания записи заполняется автоматически",
    )
    level = models.PositiveIntegerField(
        verbose_name="Уровень звена",
        help_text="Укажите уровень звена от 0 до 2 (Завод всегда равен 0)",
        **NULLABLE,
    )
    products = models.ManyToManyField(
        Product,
        verbose_name="Продукты",
        help_text="Выберите продукты",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.name
