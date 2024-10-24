from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("u400", views.U400ModelViewSet, basename="u400")
router.register("u700", views.U700ModelViewSet, basename="u700")
router.register("u800", views.U800ModelViewSet, basename="u800")
router.register("u950", views.U950ModelViewSet, basename="u950")
router.register("u970", views.U970ModelViewSet, basename="u970")

router.register("unit", views.DailyDataPxViewSet, basename="unit")


urlpatterns = router.urls
