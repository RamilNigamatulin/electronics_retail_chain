from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from electronics.models import Product, NetworkElectronics
from electronics.paginations import ElectronicsPagination

from electronics.serializers import (
    NetworkElectronicsSerializer,
    ProductSerializer,
    NetworkElectronicsDetailSerializer,
)
from users.permissions import IsActiveEmployee


class NetworkElectronicsCreateAPIView(CreateAPIView):
    """Создаем новую организацию."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer
    permission_classes = [IsActiveEmployee]


class NetworkElectronicsListAPIView(ListAPIView):
    """Выводим список всех организаций."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer
    permission_classes = [IsActiveEmployee]
    pagination_class = ElectronicsPagination

    # Создаем фильтр-поиск по стране
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "country",
    ]


class NetworkElectronicsUpdateAPIView(UpdateAPIView):
    """Редактируем организацию."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer
    permission_classes = [IsActiveEmployee]


class NetworkElectronicsRetrieveAPIView(RetrieveAPIView):
    """Выводим одну организацию."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsDetailSerializer
    permission_classes = [IsActiveEmployee]


class NetworkElectronicsDestroyAPIView(DestroyAPIView):
    """Удаляем организацию."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer
    permission_classes = [IsActiveEmployee]


class ProductCreateAPIView(CreateAPIView):
    """Создаем новый продукт."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class ProductListAPIView(ListAPIView):
    """Выводим список всех продуктов."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
    pagination_class = ElectronicsPagination


class ProductUpdateAPIView(UpdateAPIView):
    """Редактируем продукт."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class ProductRetrieveAPIView(RetrieveAPIView):
    """Выводим один продукт."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class ProductDestroyAPIView(DestroyAPIView):
    """Удаляем продукт."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
