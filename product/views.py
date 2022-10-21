from ngram import NGram
import string
from .models import Product
from computer.models import Computer, CPU, Disk, Memory
from default.models import Brand, OS
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

osList = ["Freedos", "Windows", "MacOS", "Linux", "ChromeOS"]
brands = ["Dell", "Acer", "Apple", "Asus", "HP", "Monster", "Lenovo", "Msi"]


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
        screen_size = self.request.query_params.get('screen_size', None)
        image = self.request.query_params.get('image', None)

        if OS.objects.filter(name=self.ngram_compare(os)).exists():
            print('OS exists')
            created_os = OS.objects.get(name=self.ngram_compare(os))
        else:
            print('OS does not exist')
            created_os = OS.objects.create(name=self.ngram_compare(os))

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

        if Brand.objects.filter(name=self.ngram_compare_brand(given_brand=brand)).exists():
            print('Brand exists')
            created_brand = Brand.objects.get(name=self.ngram_compare_brand(given_brand=brand))
        else:
            print('Brand does not exist')
            created_brand = Brand.objects.create(name=self.ngram_compare_brand(given_brand=brand))

        if Computer.objects.filter(model_number=model_number, serial_number=serial_number, brand=created_brand,
                                   cpu=created_cpu, disk=created_disk, memory=created_memory, os=created_os,
                                   screen_size=screen_size).exists():
            print('Computer exists')
            created_computer = Computer.objects.get(model_number=model_number, serial_number=serial_number,
                                                    brand=created_brand, cpu=created_cpu, disk=created_disk,
                                                    memory=created_memory, os=created_os, screen_size=screen_size)
        else:
            print('Computer does not exist')
            created_computer = Computer.objects.create(model_number=model_number, serial_number=serial_number,
                                                       brand=created_brand, cpu=created_cpu, disk=created_disk,
                                                       memory=created_memory, os=created_os, screen_size=screen_size)

        if Product.objects.filter(computer=created_computer, url=url).exists():
            print('Product exists')
            return Product.objects.filter(computer=created_computer, url=url)
        else:
            print('Product does not exist')
            Product.objects.create(computer=created_computer, url=url, price=price, website=website, score=score,
                                   image=image)
            return Product.objects.filter(computer=created_computer, url=url, website=website, image=image)

    def ngram_compare(self, os):
        print(os)
        for system in osList:
            result = NGram.compare(system.lower(), os.lower().replace(" ", ""))
            print(result)
            if os.lower() == 'ubuntu':
                system = 'Linux'
                return system
            elif result > 0.15:
                return system

    def ngram_compare_brand(self, given_brand):
        if given_brand.lower().strip() == 'monster':
            return 'MONSTER'
        for brand in brands:
            result = NGram.compare(brand.lower(), given_brand.lower())
            print(result)
            if result > 0.1:
                return brand.upper()


class SameProductsListaToModelNumber(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        choosenProducts = []
        search = self.request.query_params.get('search', None)

        def findMinPrice(products):
            if len(products) == 0:
                return False
            x = products[0]
            for i in range(1, len(products)):
                if x.price > products[i].price:
                    x = products[i]
            return x

        if not search:
            return Product.objects.all()
        for product in Product.objects.all():
            if product.computer.model_number.lower() == search.lower():
                results.append(product)

        trendyol = [i for i in results if i.website.lower() == 'Trendyol'.lower()]
        vatan = [i for i in results if i.website.lower() == 'Vatan Bilgisayar'.lower()]
        n11 = [i for i in results if i.website.lower() == 'n11'.lower()]
        teknosa = [i for i in results if i.website.lower() == 'Teknosa'.lower()]

        choosenTrendyol = findMinPrice(trendyol)
        choosenVatan = findMinPrice(vatan)
        choosenN11 = findMinPrice(n11)
        choosenTeknosa = findMinPrice(teknosa)

        if choosenTrendyol:
            choosenProducts.append(choosenTrendyol)
        if choosenVatan:
            choosenProducts.append(choosenVatan)
        if choosenN11:
            choosenProducts.append(choosenN11)
        if choosenTeknosa:
            choosenProducts.append(choosenTeknosa)

        return choosenProducts


class SameProductsListaToModelNumberIncludes(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        choosenProducts = []
        search = self.request.query_params.get('search', None)

        def findMinPrice(products):
            if len(products) == 0:
                return False
            x = products[0]
            for i in range(1, len(products)):
                if x.price > products[i].price:
                    x = products[i]
            return x

        if not search:
            return Product.objects.all()
        for product in Product.objects.all():
            searchInput = search.lower().replace(" ", "").translate(str.maketrans('', '', string.punctuation))
            comparedInput = product.computer.model_number.lower().replace(" ", "").translate(
                str.maketrans('', '', string.punctuation))
            print(searchInput, comparedInput)
            if searchInput in comparedInput:
                results.append(product)

        trendyol = [i for i in results if i.website.lower() == 'Trendyol'.lower()]
        vatan = [i for i in results if i.website.lower() == 'Vatan Bilgisayar'.lower()]
        n11 = [i for i in results if i.website.lower() == 'n11'.lower()]
        teknosa = [i for i in results if i.website.lower() == 'Teknosa'.lower()]

        choosenTrendyol = findMinPrice(trendyol)
        choosenVatan = findMinPrice(vatan)
        choosenN11 = findMinPrice(n11)
        choosenTeknosa = findMinPrice(teknosa)

        if choosenTrendyol:
            choosenProducts.append(choosenTrendyol)
        if choosenVatan:
            choosenProducts.append(choosenVatan)
        if choosenN11:
            choosenProducts.append(choosenN11)
        if choosenTeknosa:
            choosenProducts.append(choosenTeknosa)

        return choosenProducts


class ProductParamsWithBrands(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_brands = self.request.query_params.get('brands', None)
        if not query_brands:
            return Product.objects.all()
        else:
            for product in Product.objects.all():
                if product.computer.brand.name.lower() in query_brands.lower():
                    results.append(product)
            return results


class ProductParamsWithPoints(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_points = self.request.query_params.get('points', None)
        if not query_points:
            return Product.objects.all()
        else:
            for product in Product.objects.all():
                if product.score >= float(query_points):
                    results.append(product)
            return results


class ProductParamsWithPrices(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_prices_start = self.request.query_params.get('price_start', None)
        query_prices_end = self.request.query_params.get('price_end', None)
        if not query_prices_start and not query_prices_end:
            return Product.objects.all()
        else:
            for product in Product.objects.all():
                if float(query_prices_start) <= product.price <= float(query_prices_end):
                    results.append(product)
            return results


class ProductParamsWithOS(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_os = self.request.query_params.get('os', None)
        if not query_os:
            return Product.objects.all()
        else:
            for product in Product.objects.all():
                if product.computer.os.name.lower() in query_os.lower():
                    results.append(product)
            return results


class ProductParamsWithMemory(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):

        results = []
        query_memory = self.request.query_params.get('memory', None)
        query = query_memory.lower().split(' ')
        print(query)
        if not query_memory:
            return Product.objects.all()
        else:
            for product in Product.objects.all():
                if product.computer.memory.memory_size.lower() in [i for i in query if i is not None]:
                    results.append(product)
            return results


class ProductParamsWithDisk(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_disk_type = self.request.query_params.get('disk_type', None)
        query_disk_size = self.request.query_params.get('disk_size', None)
        if not query_disk_type or not query_disk_size:
            return Product.objects.all()
        else:

            for product in Product.objects.all():
                print(query_disk_type.lower(), product.computer.disk.disk_type.lower().replace(' ', ''))
                print(query_disk_size.lower(), product.computer.disk.disk_size.lower().replace(' ', ''))
                if product.computer.disk.disk_type.lower().replace(' ',
                                                                   '') == query_disk_type.lower() and query_disk_size.lower().replace(
                    ' ', '+') in product.computer.disk.disk_size.lower().replace(' ', ''):
                    results.append(product)
            return results


class ProductParamsCheapest(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_cheapest = self.request.query_params.get('cheap', None)
        if not query_cheapest:
            return Product.objects.all()
        else:
            sortProducts = sorted(Product.objects.all(), key=lambda x: x.price)
            for i in range(len(sortProducts)):
                results.append(sortProducts[i])
            return results


class ProductParamsExpensive(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_expensive = self.request.query_params.get('expensive', None)
        if not query_expensive:
            return Product.objects.all()
        else:
            sortProducts = sorted(Product.objects.all(), key=lambda x: x.price, reverse=True)
            for i in range(len(sortProducts)):
                results.append(sortProducts[i])
            return results


class ProductParamsScore(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_score = self.request.query_params.get('score', None)
        if not query_score:
            return Product.objects.all()
        else:
            sortProducts = sorted(Product.objects.all(), key=lambda x: x.score, reverse=True)
            for i in range(len(sortProducts)):
                results.append(sortProducts[i])
            return results




class ProductParamsWithCPU(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_cpu = self.request.query_params.get('cpu', None)
        if not query_cpu:
            return Product.objects.all()
        else:

            for product in Product.objects.all():
                print(product.computer.cpu.cpu_type.lower())
                if query_cpu.lower() in product.computer.cpu.cpu_type.lower():
                    results.append(product)
            return results


class ProductsMultiParameters(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        results = []
        query_brands = self.request.query_params.get('brands', None)
        query_points = self.request.query_params.get('points', None)
        query_prices_start = self.request.query_params.get('price_start', None)
        query_prices_end = self.request.query_params.get('price_end', None)
        query_os = self.request.query_params.get('os', None)
        query_memory = self.request.query_params.get('memory', None)
        query_disk_type = self.request.query_params.get('disk_type', None)
        query_disk_size = self.request.query_params.get('disk_size', None)
        query_cheapest = self.request.query_params.get('cheap', None)
        query_expensive = self.request.query_params.get('expensive', None)
        query_score = self.request.query_params.get('score', None)

        if not query_brands and not query_points and not query_prices_start and not query_prices_end and not query_os and not query_memory and not query_disk_type and not query_disk_size and not query_cheapest and not query_expensive and not query_score:
            return Product.objects.all()
        else:
            for product in Product.objects.all():
                if query_brands:
                    if product.computer.brand.name.lower() in query_brands.lower():
                        results.append(product)
                if query_points:
                    if product.score >= float(query_points):
                        results.append(product)
                if query_prices_start and query_prices_end:
                    if float(query_prices_start) <= product.price <= float(query_prices_end):
                        results.append(product)
                if query_os:
                    if product.computer.os.name.lower() in query_os.lower():
                        results.append(product)
                if query_memory:
                    query = query_memory.lower().split(' ')
                    if product.computer.memory.memory_size.lower() in [i for i in query if i is not None]:
                        results.append(product)
                if query_disk_type and query_disk_size:
                    if product.computer.disk.disk_type.lower().replace(' ',
                                                                       '') == query_disk_type.lower() and query_disk_size.lower().replace(
                            ' ', '+') in product.computer.disk.disk_size.lower().replace(' ', ''):
                        results.append(product)
            return results


