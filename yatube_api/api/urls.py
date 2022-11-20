from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

app_name = 'api'

router = DefaultRouter()
router.register('v1/posts', PostViewSet)
router.register(r'v1/posts/(?P<post_id>[1-9]\d*)/comments', CommentViewSet,
                basename='comments')
router.register('v1/groups', GroupViewSet)
router.register('v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
