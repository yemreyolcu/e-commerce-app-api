from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Computer, CPU, Disk, Memory
from default.serializers import BrandSerializer, OSSerializer


class ComputerSerializer(ModelSerializer):
    brand_data = SerializerMethodField(method_name='get_brand_data')
    cpu_data = SerializerMethodField(method_name='get_cpu_data')
    disk_data = SerializerMethodField(method_name='get_disk_data')
    memory_data = SerializerMethodField(method_name='get_memory_data')
    os_data = SerializerMethodField(method_name='get_os_data')

    class Meta:
        model = Computer
        fields = (
            'id', 'model_number', 'serial_number', 'brand', 'cpu', 'disk', 'memory', 'os', 'screen_size', 'os_data',
            'brand_data',
            'cpu_data', 'disk_data', 'memory_data')

    def get_brand_data(self, obj):
        return BrandSerializer(obj.brand).data

    def get_cpu_data(self, obj):
        return CPUSerializer(obj.cpu).data

    def get_disk_data(self, obj):
        return DiskSerializer(obj.disk).data

    def get_memory_data(self, obj):
        return MemorySerializer(obj.memory).data

    def get_os_data(self, obj):
        return OSSerializer(obj.os).data


class CPUSerializer(ModelSerializer):
    class Meta:
        model = CPU
        fields = ['id', 'cpu_type', 'cpu_generation']


class DiskSerializer(ModelSerializer):
    class Meta:
        model = Disk
        fields = ['id', 'disk_type', 'disk_size']


class MemorySerializer(ModelSerializer):
    class Meta:
        model = Memory
        fields = ['id', 'memory_size']
