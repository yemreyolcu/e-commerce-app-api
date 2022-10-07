from django.urls import path
from .views import ProductListCreate, ProductRetrieveAPIView, ProductRetrieveUpdateDestroy, ProductReadyToDeployList

urlpatterns = [
    path('productlistcreate/', ProductListCreate.as_view()),
    path('productretrieve/<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('productretrieveupdatedestroy/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
    path('productreadytodeploylist/', ProductReadyToDeployList.as_view()),
]
