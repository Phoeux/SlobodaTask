from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from urllib.parse import urlparse

from api.models import Review, Shop
from api.serializers import ReviewSerializer, ShopSerializer
from api.utils import get_shop


class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user', 'shop_link']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        domain = urlparse(self.request.data['shop_link']).netloc
        get_shop(self, domain)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        domain = urlparse(serializer.data['shop_link']).netloc
        get_shop(self, domain)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        domain = urlparse(instance.shop_link).netloc
        get_shop(self, domain)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupByUser(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = self.queryset.order_by('user', '-creation_time')
        return queryset


class ShopList(viewsets.ReadOnlyModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [OrderingFilter]
