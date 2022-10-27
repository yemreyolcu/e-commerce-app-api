from django.shortcuts import render
from .serializers import BrandSerializer, OSSerializer
from .models import Brand, OS
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView


# Create your views here.


class BrandListCreateAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def perform_create(self, serializer):
        name = self.request.data.get('name').upper().replace(" ", "")
        if Brand.objects.filter(name=name).exists():
            print("Brand already exists")
            sameBrands = Brand.objects.filter(name=name)
            print(sameBrands)
            if sameBrands.count() > 1:
                print("There are more than one same brands")
                for brand in enumerate(sameBrands):
                    if brand[0] == 0:
                        print("First brand")
                        continue
                    else:
                        print("Duplicate brand")
                        brand[1].delete()
        else:
            print("Brand does not exist")
            serializer.save(name=name.upper().replace(" ", ""))



class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'


class BrandRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'


class BrandRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'


class OSListCreateAPIView(ListCreateAPIView):
    queryset = OS.objects.all()
    serializer_class = OSSerializer

    def perform_create(self, serializer):
        print("OSListCreateAPIView")
        name = self.request.data.get('name').upper().replace(" ", "")
        if OS.objects.filter(name=name).exists():
            print("OS already exists")
            sameOS = OS.objects.filter(name=name)
            print(sameOS)
            if sameOS.count() > 1:
                print("There are more than one same OS")
                for os in enumerate(sameOS):
                    if os[0] == 0:
                        print("First OS")
                        continue
                    else:
                        print("Duplicate OS")
                        os[1].delete()
        else:
            print("OS does not exist")
            serializer.save(name=name.upper().replace(" ", ""))


class OSRetrieveAPIView(RetrieveAPIView):
    queryset = OS.objects.all()
    serializer_class = OSSerializer
    lookup_field = 'pk'


class OSRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = OS.objects.all()
    serializer_class = OSSerializer
    lookup_field = 'pk'


class OSRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = OS.objects.all()
    serializer_class = OSSerializer
    lookup_field = 'pk'
