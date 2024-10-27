from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .excel_views import export_to_excel

router = DefaultRouter()


# help text router

router.register("helptext/u400", views.U400HelpTextViewSet, basename="help_u400")
router.register("helptext/u700", views.U700HelpTextViewSet, basename="help_u700")
router.register("helptext/u800", views.U800HelpTextViewSet, basename="help_u800")
router.register("helptext/u950", views.U950HelpTextViewSet, basename="help_u950")
router.register("helptext/u970", views.U970HelpTextViewSet, basename="help_u970")


# unit route


router.register("u400", views.U400ModelViewSet, basename="u400")
router.register("u700", views.U700ModelViewSet, basename="u700")
router.register("u800", views.U800ModelViewSet, basename="u800")
router.register("u950", views.U950ModelViewSet, basename="u950")
router.register("u970", views.U970ModelViewSet, basename="u970")

router.register("unit", views.DailyDataPxViewSet, basename="unit")


# Combine router URLs with additional paths
urlpatterns = [
    path("", include(router.urls)),  # Include all the router URLs
    path(
        "download_monthly_data/", export_to_excel, name="download_monthly_data"
    ),  # Excel download path
]
