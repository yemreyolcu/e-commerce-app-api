from django.shortcuts import render
from .serializers import BrandSerializer, OSSerializer
from .models import Brand, OS
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView


# Create your views here.


class BrandListCreateAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


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
