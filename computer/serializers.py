from rest_framework.serializers import ModelSerializer
from .models import Computer, CPU, Disk, Memory


class ComputerSerializer(ModelSerializer):

    class Meta:
        model = Computer
        fields = ['id', 'model_number', 'serial_number', 'brand', 'cpu', 'disk', 'memory']


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
