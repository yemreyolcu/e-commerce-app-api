from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveAPIView
from .models import Computer, CPU, Disk, Memory
from .serializers import ComputerSerializer, CPUSerializer, DiskSerializer, MemorySerializer


class ComputerListCreate(ListCreateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    lookup_field = 'pk'


class ComputerRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    lookup_field = 'pk'


class ComputerRetrieve(RetrieveAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    lookup_field = 'pk'


class CPUListCreateAPIView(ListCreateAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class CPURetrieve(RetrieveAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    lookup_field = 'pk'


class CPUUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    lookup_field = 'pk'


class CPUDeleteAPIView(RetrieveDestroyAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    lookup_field = 'pk'


class DiskListCreateAPIView(ListCreateAPIView):
    queryset = Disk.objects.all()
    serializer_class = DiskSerializer


class DiskRetrieve(RetrieveAPIView):
    queryset = Disk.objects.all()
    serializer_class = DiskSerializer
    lookup_field = 'pk'


class DiskUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Disk.objects.all()
    serializer_class = DiskSerializer
    lookup_field = 'pk'


class DiskDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Disk.objects.all()
    serializer_class = DiskSerializer
    lookup_field = 'pk'


class MemoryListCreateAPIView(ListCreateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class MemoryRetrieve(RetrieveAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    lookup_field = 'pk'


class MemoryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    lookup_field = 'pk'


class MemoryDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    lookup_field = 'pk'
