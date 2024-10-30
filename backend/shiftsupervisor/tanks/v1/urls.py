from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AdditionalServicesViewSet, ServiceConsumedAndShippedDailyViewSet, 
    ProductViewSet, ProductProducedAndShippedDailyViewSet, TankerViewSet, 
    CargoLoadingViewSet, TankViewSet, TankInventoryViewSet, 
    FeedViewSet, FeedReceptionViewSet
)

router = DefaultRouter()
router.register('additional-services', AdditionalServicesViewSet)
router.register('service-consumed-shipped', ServiceConsumedAndShippedDailyViewSet)
router.register('products', ProductViewSet)
router.register('product-produced-shipped', ProductProducedAndShippedDailyViewSet)
router.register('tankers', TankerViewSet)
router.register('cargo-loading', CargoLoadingViewSet)
router.register('tanks', TankViewSet)
router.register('tank-inventory', TankInventoryViewSet)
router.register('feeds', FeedViewSet)
router.register('feed-receptions', FeedReceptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
