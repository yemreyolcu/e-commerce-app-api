from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product
from default.serializers import BrandSerializer, OSSerializer
from computer.serializers import ComputerSerializer, CPUSerializer, DiskSerializer, MemorySerializer


class ProductSerializer(ModelSerializer):
    brand_data = SerializerMethodField(method_name='get_brand_data')
    computer_data = SerializerMethodField(method_name='get_computer_data')
    os_data = SerializerMethodField(method_name='get_os_data')
    cpu_data = SerializerMethodField(method_name='get_cpu_data')
    memory_data = SerializerMethodField(method_name='get_memory_data')
    disk_data = SerializerMethodField(method_name='get_disk_data')

    class Meta:
        model = Product
        fields = ['id', 'brand', 'computer', 'os', 'cpu', 'memory', 'disk', 'score', 'price', 'website', 'brand_data',
                  'computer_data', 'os_data', 'cpu_data', 'memory_data', 'disk_data']

    def get_brand_data(self, obj):
        return BrandSerializer(obj.brand).data

    def get_computer_data(self, obj):
        return ComputerSerializer(obj.computer).data

    def get_os_data(self, obj):
        return OSSerializer(obj.os).data

    def get_cpu_data(self, obj):
        return CPUSerializer(obj.cpu).data

    def get_memory_data(self, obj):
        return MemorySerializer(obj.memory).data

    def get_disk_data(self, obj):
        return DiskSerializer(obj.disk).data
