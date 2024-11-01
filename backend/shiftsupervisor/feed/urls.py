from django.urls import include,path


app_name = "feed"

urlpatterns = [
    path("api/v1/", include("feed.api.v1.urls")),
]