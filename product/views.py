from ngram import NGram

from .models import Product
from computer.models import Computer, CPU, Disk, Memory
from default.models import Brand, OS
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView


# osList = ["Freedos", "Windows", "MacOS", "Linux"]


class ProductListCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductReadyToDeployList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    """ def check_duplicate(self, os):
        for system in osList:
            result = NGram.compare(system, os.strip())
            print(result)
            if result > 0.3:
                print(system)
                return system
            else:
                return "Other" """

    def get_queryset(self):
        cpu_type = self.request.query_params.get('cpu_type', None)
        cpu_generation = self.request.query_params.get('cpu_generation', None)
        disk_type = self.request.query_params.get('disk_type', None)
        disk_size = self.request.query_params.get('disk_size', None)
        memory_size = self.request.query_params.get('memory_size', None)
        brand = self.request.query_params.get('brand', None)
        os = self.request.query_params.get('os', None)
        model_number = self.request.query_params.get('model_number', None)
        serial_number = self.request.query_params.get('serial_number', None)
        url = self.request.query_params.get('url', None)
        price = self.request.query_params.get('price', None)
        website = self.request.query_params.get('website', None)
        score = self.request.query_params.get('score', None)

        if CPU.objects.filter(cpu_type=cpu_type, cpu_generation=cpu_generation).exists():
            print('CPU exists')
            created_cpu = CPU.objects.get(cpu_type=cpu_type, cpu_generation=cpu_generation)
        else:
            print('CPU does not exist')
            created_cpu = CPU.objects.create(cpu_type=cpu_type, cpu_generation=cpu_generation)

        if Disk.objects.filter(disk_type=disk_type, disk_size=disk_size).exists():
            print('Disk exists')
            created_disk = Disk.objects.get(disk_type=disk_type, disk_size=disk_size)
        else:
            print('Disk does not exist')
            created_disk = Disk.objects.create(disk_type=disk_type, disk_size=disk_size)

        if Memory.objects.filter(memory_size=memory_size).exists():
            print('Memory exists')
            created_memory = Memory.objects.get(memory_size=memory_size)
        else:
            print('Memory does not exist')
            created_memory = Memory.objects.create(memory_size=memory_size)

        if Brand.objects.filter(name=brand).exists():
            print('Brand exists')
            created_brand = Brand.objects.get(name=brand)
        else:
            print('Brand does not exist')
            created_brand = Brand.objects.create(name=brand)

        if OS.objects.filter(name=os).exists():
            print('OS exists')
            created_os = OS.objects.get(name=os)
        else:
            print('OS does not exist')
            created_os = OS.objects.create(name=os)

        if Computer.objects.filter(model_number=model_number, serial_number=serial_number, brand=created_brand,
                                   cpu=created_cpu, disk=created_disk, memory=created_memory, os=created_os).exists():
            print('Computer exists')
            created_computer = Computer.objects.get(model_number=model_number, serial_number=serial_number,
                                                    brand=created_brand, cpu=created_cpu, disk=created_disk,
                                                    memory=created_memory, os=created_os)
        else:
            print('Computer does not exist')
            created_computer = Computer.objects.create(model_number=model_number, serial_number=serial_number,
                                                       brand=created_brand, cpu=created_cpu, disk=created_disk,
                                                       memory=created_memory, os=created_os)

        if Product.objects.filter(computer=created_computer, url=url).exists():
            print('Product exists')
            return Product.objects.filter(computer=created_computer, url=url, os=created_os)
        else:
            print('Product does not exist')
            Product.objects.create(computer=created_computer, url=url, price=price, website=website, score=score)
            return Product.objects.filter(computer=created_computer, url=url, website=website)
