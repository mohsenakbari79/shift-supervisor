from django.urls import include,path


app_name = "tank"

urlpatterns = [
    path("api/v1/", include("tanks.api.v1.urls")),
]