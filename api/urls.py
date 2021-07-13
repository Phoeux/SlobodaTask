from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('review', views.ReviewModelViewSet, basename='review'),


urlpatterns = [
    path('', include((router.urls, 'api'))),
    path('group_by_user', views.GroupByUser.as_view(), name='grp_user')
]