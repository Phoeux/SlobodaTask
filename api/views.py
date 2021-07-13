from rest_framework import viewsets

from api.models import Review
from api.serializers import ReviewSerializer


class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
