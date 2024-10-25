from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# help text router

router.register("helptext/u100", views.U100HelpTextViewSet, basename="help_u100")
router.register("helptext/u200", views.U200HelpTextViewSet, basename="help_u200")
router.register("helptext/u250", views.U250HelpTextViewSet, basename="help_u250")
router.register("helptext/u300", views.U300HelpTextViewSet, basename="help_u300")
router.register("helptext/u350", views.U350HelpTextViewSet, basename="help_u350")


# unit route
router.register("u100", views.U100ModelViewSet, basename="u100")
router.register("u200", views.U200ModelViewSet, basename="u200")
router.register("u250", views.U250ModelViewSet, basename="u250")
router.register("u300", views.U300ModelViewSet, basename="u300")
router.register("u350", views.U350ModelViewSet, basename="u350")
router.register("unit", views.DailyDataReformingViewSet, basename="unit")


urlpatterns = router.urls
