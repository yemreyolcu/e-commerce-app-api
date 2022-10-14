from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product
from computer.serializers import ComputerSerializer


class ProductSerializer(ModelSerializer):
    computer_data = SerializerMethodField(method_name='get_computer_data')

    class Meta:
        model = Product
        fields = ['id', 'computer', 'score', 'price', 'website', 'image', 'post_image', 'computer_data', 'url']

    def get_computer_data(self, obj):
        return ComputerSerializer(obj.computer).data
