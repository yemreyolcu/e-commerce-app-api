from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveAPIView
from .models import Computer, CPU, Disk, Memory
from .serializers import ComputerSerializer, CPUSerializer, DiskSerializer, MemorySerializer


class ComputerListCreate(ListCreateAPIView):
    serializer_class = ComputerSerializer
    queryset = Computer.objects.all()

    def perform_create(self, serializer):
        mySize = self.request.data.get('screen_size') + '"'
        serializer.save(screen_size=mySize)
        model_number = self.request.data.get('model_number')
        serial_number = self.request.data.get('serial_number')
        brand = self.request.data.get('brand')
        cpu = self.request.data.get('cpu')
        disk = self.request.data.get('disk')
        memory = self.request.data.get('memory')
        os = self.request.data.get('os')
        print(model_number, serial_number, brand, cpu, disk, memory, os, mySize)

        if Computer.objects.filter(model_number=model_number, serial_number=serial_number, brand=brand, cpu=cpu,
                                   disk=disk, memory=memory, os=os, screen_size=mySize).exists():
            print("Computer already exists")
            sameComputers = Computer.objects.filter(model_number=model_number, serial_number=serial_number, brand=brand,
                                                    cpu=cpu, disk=disk, memory=memory, os=os, screen_size=mySize)
            print(sameComputers)
            if sameComputers.count() > 1:
                print("There are more than one same computers")
                for computer in enumerate(sameComputers):
                    if computer[0] == 0:
                        print("First computer")
                        continue
                    else:
                        print("Other computer")
                        computer[1].delete()

        else:
            print("Computer does not exist")

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
