from rest_framework.serializers import ModelSerializer
from .models import Brand, OS


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class OSSerializer(ModelSerializer):
    class Meta:
        model = OS
        fields = '__all__'
