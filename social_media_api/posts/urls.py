from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import CommentViewset, PostViewset

# from .views import (
#     # CreateCommentView,
#     # CreatePostView,
#     # DetailCommentView,
#     # DetailPostView,
# )

router = DefaultRouter()

# router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewset, basename="comment")
router.register(r"posts", PostViewset, basename="post")

posts_router = NestedDefaultRouter(router, r"posts", lookup="post")
posts_router.register(r"comments", CommentViewset, basename="post_comments")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
    # path("add_comment/", CreateCommentView.as_view(), name="add_comment"),
    # path(
    #     "update_comment/<int:id>/",
    #     DetailCommentView.as_view(),
    #     name="update_comment",
    # ),
    # path("add_post/", CreatePostView.as_view(), name="add_post"),
    # path(
    #     "update_post/<int:id>/",
    #     DetailPostView.as_view(),
    #     name="update_comment",
    # ),
]
