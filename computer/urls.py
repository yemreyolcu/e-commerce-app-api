from django.urls import path
from .views import ComputerListCreate, ComputerRetrieveUpdate, ComputerRetrieveDestroy, ComputerRetrieve, \
    CPUListCreateAPIView, CPURetrieve, CPUUpdateAPIView, CPUDeleteAPIView, DiskListCreateAPIView, DiskRetrieve, \
    DiskUpdateAPIView, DiskDeleteAPIView, MemoryListCreateAPIView, MemoryRetrieve, MemoryUpdateAPIView, MemoryDeleteAPIView
urlpatterns = [
    path('computerlistcreate/', ComputerListCreate.as_view()),
    path('computerretrieveupdate/<int:pk>/', ComputerRetrieveUpdate.as_view()),
    path('computerretrievedestroy/<int:pk>/', ComputerRetrieveDestroy.as_view()),
    path('computerretrieve/<int:pk>/', ComputerRetrieve.as_view()),
    path('cpulistcreate/', CPUListCreateAPIView.as_view()),
    path('cpuretrieve/<int:pk>/', CPURetrieve.as_view()),
    path('cpuupdate/<int:pk>/', CPUUpdateAPIView.as_view()),
    path('cpudelete/<int:pk>/', CPUDeleteAPIView.as_view()),
    path('disklistcreate/', DiskListCreateAPIView.as_view()),
    path('diskretrieve/<int:pk>/', DiskRetrieve.as_view()),
    path('diskupdate/<int:pk>/', DiskUpdateAPIView.as_view()),
    path('diskdelete/<int:pk>/', DiskDeleteAPIView.as_view()),
    path('memorylistcreate/', MemoryListCreateAPIView.as_view()),
    path('memoryretrieve/<int:pk>/', MemoryRetrieve.as_view()),
    path('memoryupdate/<int:pk>/', MemoryUpdateAPIView.as_view()),
    path('memorydelete/<int:pk>/', MemoryDeleteAPIView.as_view()),
]
