from django.urls import include,path


app_name = "btx"

urlpatterns = [
    path("api/v1/", include("btx.api.v1.urls")),
]