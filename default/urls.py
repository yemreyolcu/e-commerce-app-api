from django.urls import path
from .views import BrandListCreateAPIView, BrandRetrieveAPIView, BrandRetrieveUpdateAPIView, \
    BrandRetrieveDestroyAPIView, OSListCreateAPIView, OSRetrieveAPIView, OSRetrieveUpdateAPIView, \
    OSRetrieveDestroyAPIView

urlpatterns = [
    path('brandlistcreate/', BrandListCreateAPIView.as_view()),
    path('brandretrieve/<int:pk>/', BrandRetrieveAPIView.as_view()),
    path('brandretrieveupdate/<int:pk>/', BrandRetrieveUpdateAPIView.as_view()),
    path('brandretrievedestroy/<int:pk>/', BrandRetrieveDestroyAPIView.as_view()),
    path('oslistcreate/', OSListCreateAPIView.as_view()),
    path('osretrieve/<int:pk>/', OSRetrieveAPIView.as_view()),
    path('osretrieveupdate/<int:pk>/', OSRetrieveUpdateAPIView.as_view()),
    path('osretrievedestroy/<int:pk>/', OSRetrieveDestroyAPIView.as_view()),
]
