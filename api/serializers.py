from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from api.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        model = Review
        fields = '__all__'
