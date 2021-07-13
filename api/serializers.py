from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
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
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['domain', 'reviews', 'avg_rate']

    def get_avg_rate(self, data):
        data.avg_rate = Review.objects.filter(shop_link__contains=data.domain).aggregate(Avg('rating'))['rating__avg']
        return data.avg_rate
