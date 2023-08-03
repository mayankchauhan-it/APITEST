from rest_framework import serializers
from .models import Brand, BrandImage

class BrandImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandImage
        fields = ['image']

class BrandSerializer(serializers.ModelSerializer):
    images = BrandImageSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'
