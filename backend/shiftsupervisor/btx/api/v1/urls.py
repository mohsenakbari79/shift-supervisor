from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views
from .excel_views import export_to_excel


router = DefaultRouter()


# help text router

router.register("helptext/u500", views.U500HelpTextViewSet, basename="help_u500")
router.register("helptext/u600", views.U600HelpTextViewSet, basename="help_u600")
router.register("helptext/u650", views.U650HelpTextViewSet, basename="help_u650")


# unit route

router.register("u500", views.U500ModelViewSet, basename="u500")
router.register("U600", views.U600ModelViewSet, basename="u600")
router.register("U650", views.U650ModelViewSet, basename="u650")
router.register("unit", views.DailyDataBtxViewSet, basename="unit")


# Combine router URLs with additional paths
urlpatterns = [
    path("", include(router.urls)),  # Include all the router URLs
    path(
        "download_monthly_data/", export_to_excel, name="download_monthly_data"
    ),  # Excel download path
]
