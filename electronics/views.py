from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from electronics.models import Product, NetworkElectronics

from electronics.serializers import (
    NetworkElectronicsSerializer,
    ProductSerializer,
)


class NetworkElectronicsCreateAPIView(CreateAPIView):
    """Создаем новую организацию."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer



class NetworkElectronicsListAPIView(ListAPIView):
    """Выводим список всех организаций."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer

    # Создаем фильтр-поиск по городу
    filter_backends = [filters.SearchFilter]
    search_fields = ['city']


class NetworkElectronicsUpdateAPIView(UpdateAPIView):
    """Редактируем организацию."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer


class NetworkElectronicsRetrieveAPIView(RetrieveAPIView):
    """Выводим одну организацию."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer


class NetworkElectronicsDestroyAPIView(DestroyAPIView):
    """Удаляем организацию."""

    queryset = NetworkElectronics.objects.all()
    serializer_class = NetworkElectronicsSerializer


class ProductCreateAPIView(CreateAPIView):
    """Создаем новый продукт."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    """Выводим список всех продуктов."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    """Редактируем продукт."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    """Выводим один продукт."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(DestroyAPIView):
    """Удаляем продукт."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
