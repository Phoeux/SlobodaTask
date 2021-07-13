from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from api.models import Review, Shop


class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    creation_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    domain = serializers.CharField(read_only=True)

    class Meta:
        model = Shop
        fields = ['domain', 'reviews', 'avg_rate']

