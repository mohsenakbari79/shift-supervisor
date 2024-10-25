from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("u100", views.U100ModelViewSet, basename="u100")
router.register("u200", views.U200ModelViewSet, basename="u200")
router.register("u250", views.U250ModelViewSet, basename="u250")
router.register("u300", views.U300ModelViewSet, basename="u300")
router.register("u350", views.U350ModelViewSet, basename="u350")

router.register("unit", views.DailyDataReformingViewSet, basename="unit")


urlpatterns = router.urls
