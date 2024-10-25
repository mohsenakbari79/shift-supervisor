from django.urls import include,path


app_name = "reforming"

urlpatterns = [
    path("api/v1/", include("reforming.api.v1.urls")),
]