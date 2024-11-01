from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet,
    TankInventoryViewSet,
    CompanyFuelAnalysisViewSet,
    TankOperationViewSet,
    GlobalFuelAnalysisViewSet,
    FeedInventoryView
)

router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('tank-inventories', TankInventoryViewSet, basename='tank-inventory')
router.register('company-fuel-analyses', CompanyFuelAnalysisViewSet, basename='company-fuel-analysis')
router.register('tank-operations', TankOperationViewSet, basename='tank-operation')
router.register('global-fuel-analyses', GlobalFuelAnalysisViewSet, basename='global-fuel-analysis')

urlpatterns = [
    path('', include(router.urls)),
    path('feed-inventory/', FeedInventoryView.as_view(), name='feed-inventory'),
]
