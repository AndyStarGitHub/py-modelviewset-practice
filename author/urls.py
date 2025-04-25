from django.urls import path, include
from rest_framework import routers
from author.views import AuthorViewSet

app_name = "author"

# router = routers.DefaultRouter()
# router.register("authors", AuthorViewSet)

author_list = AuthorViewSet.as_view(actions={"get": "list", "post": "create"})
author_detail = AuthorViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
        "patch": "partial_update",
    }
)

urlpatterns = [
    # path("", include(router.urls)),
    path("authors/", author_list, name="manage-list"),
    path("authors/<int:pk>/", author_detail, name="manage-list"),
]
