from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AdditionalServicesViewSet,
    ServiceConsumedAndShippedDailyView,
    ProductViewSet,
    ProductProducedAndShippedDailyModelViewSet,
    ProductProducedAndShippedDailyViewSet,
    TankerViewSet,
    CargoLoadingViewSet,
    TankViewSet,
    TankInventoryViewSet,
)

router = DefaultRouter()
router.register('additional-services', AdditionalServicesViewSet, basename='additional-service')
router.register('products', ProductViewSet, basename='product')
router.register('products-produced-and-shipped', ProductProducedAndShippedDailyModelViewSet, basename='product-produced-and-shipped')
router.register('tankers', TankerViewSet, basename='tanker')
router.register('cargo-loading', CargoLoadingViewSet, basename='cargo-loading')
router.register('tanks', TankViewSet, basename='tank')
router.register('tank-inventories', TankInventoryViewSet, basename='tank-inventory')

urlpatterns = [
    path('', include(router.urls)),
    path('service-consumed-and-shipped-daily/', ServiceConsumedAndShippedDailyView.as_view(), name='service-consumed-and-shipped-daily'),
    path('product-produced-and-shipped-daily/', ProductProducedAndShippedDailyViewSet.as_view(), name='product-produced-and-shipped-daily'),
]
