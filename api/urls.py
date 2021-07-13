from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('review', views.ReviewModelViewSet, basename='review'),
router.register('shop', views.ShopList, basename='shop'),
router.register('group_by_user', views.GroupByUser, basename='group')


urlpatterns = [
    path('', include((router.urls, 'api'))),
]