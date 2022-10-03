from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Computer, CPU, Disk, Memory


class ComputerSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = ['id', 'model_number', 'serial_number']


class CPUSerializer(ModelSerializer):
    computer_data = SerializerMethodField(method_name='get_computer_data')

    class Meta:
        model = CPU
        fields = ['id', 'cpu_type', 'cpu_generation', 'computer', 'computer_data']

    def get_computer_data(self, obj):
        return ComputerSerializer(obj.computer).data


class DiskSerializer(ModelSerializer):
    computer_data = SerializerMethodField(method_name='get_computer_data')

    class Meta:
        model = Disk
        fields = ['id', 'disk_type', 'disk_size', 'computer', 'computer_data']

    def get_computer_data(self, obj):
        return ComputerSerializer(obj.computer).data


class MemorySerializer(ModelSerializer):
    computer_data = SerializerMethodField(method_name='get_computer_data')

    class Meta:
        model = Memory
        fields = ['id', 'memory_size', 'computer', 'computer_data']

    def get_computer_data(self, obj):
        return ComputerSerializer(obj.computer).data
