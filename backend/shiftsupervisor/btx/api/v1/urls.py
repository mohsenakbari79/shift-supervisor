from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("u500", views.U500ModelViewSet, basename="u500")
router.register("U650", views.U600ModelViewSet, basename="u600")
router.register("U650", views.U650ModelViewSet, basename="u650")
router.register("unit", views.DailyDataBtxViewSet, basename="unit")


urlpatterns = router.urls