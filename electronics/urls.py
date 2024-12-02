from django.urls import path

from electronics.apps import ElectronicsConfig
from electronics.views import (
    NetworkElectronicsListAPIView,
    NetworkElectronicsRetrieveAPIView,
    NetworkElectronicsUpdateAPIView,
    NetworkElectronicsDestroyAPIView,
    NetworkElectronicsCreateAPIView,
    ProductListAPIView,
    ProductRetrieveAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    ProductCreateAPIView,
)

app_name = ElectronicsConfig.name

urlpatterns = [
    path(
        "electronics/",
        NetworkElectronicsListAPIView.as_view(),
        name="list_electronics",
    ),
    path(
        "electronics/<int:pk>/",
        NetworkElectronicsRetrieveAPIView.as_view(),
        name="retrieve_electronics",
    ),
    path(
        "electronics/<int:pk>/update/",
        NetworkElectronicsUpdateAPIView.as_view(),
        name="update_electronics",
    ),
    path(
        "electronics/<int:pk>/delete/",
        NetworkElectronicsDestroyAPIView.as_view(),
        name="delete_electronics",
    ),
    path(
        "electronics/create/",
        NetworkElectronicsCreateAPIView.as_view(),
        name="create_electronics",
    ),
    path(
        "products/",
        ProductListAPIView.as_view(),
        name="list_products",
    ),
    path(
        "products/<int:pk>/",
        ProductRetrieveAPIView.as_view(),
        name="retrieve_products",
    ),
    path(
        "products/<int:pk>/update/",
        ProductUpdateAPIView.as_view(),
        name="update_products",
    ),
    path(
        "products/<int:pk>/delete/",
        ProductDestroyAPIView.as_view(),
        name="delete_products",
    ),
    path(
        "products/create/",
        ProductCreateAPIView.as_view(),
        name="create_products",
    ),
]
