from django.urls import include,path


app_name = "px"

urlpatterns = [
    path("api/v1/", include("px.api.v1.urls")),
]