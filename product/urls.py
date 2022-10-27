from django.urls import path
from .views import ProductListCreate, ProductRetrieveAPIView, ProductRetrieveUpdateDestroy, ProductReadyToDeployList, \
    SameProductsListaToModelNumber, SameProductsListaToModelNumberIncludes, ProductParamsWithBrands, \
    ProductParamsWithPoints, ProductParamsWithPrices, ProductParamsWithOS, ProductParamsWithMemory, \
    ProductParamsWithDisk, ProductParamsCheapest, ProductParamsExpensive, ProductParamsScore, ProductParamsWithCPU, \
    ProductCreateAPIView, ProductParamsWithScreen, ProductMultiFilter

urlpatterns = [
    path('productlistcreate/', ProductListCreate.as_view()),
    path('productretrieve/<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('productretrieveupdatedestroy/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
    path('productreadytodeploylist/', ProductReadyToDeployList.as_view()),
    path('sameproductslist/', SameProductsListaToModelNumber.as_view()),
    path('sameproductslistincludes/', SameProductsListaToModelNumberIncludes.as_view()),
    path('productparamswithbrands/', ProductParamsWithBrands.as_view()),
    path('productparamswithpoints/', ProductParamsWithPoints.as_view()),
    path('productparamswithprices/', ProductParamsWithPrices.as_view()),
    path('productparamswithos/', ProductParamsWithOS.as_view()),
    path('productparamswithmemory/', ProductParamsWithMemory.as_view()),
    path('productparamswithdisk/', ProductParamsWithDisk.as_view()),
    path('productparamscheap/', ProductParamsCheapest.as_view()),
    path('productparamsexpensive/', ProductParamsExpensive.as_view()),
    path('productparamsscore/', ProductParamsScore.as_view()),
    path('productparamswithcpu/', ProductParamsWithCPU.as_view()),
    path('productparamsscreen/', ProductParamsWithScreen.as_view()),
    path('productcreate/', ProductCreateAPIView.as_view()),
    path('productmultifilter/', ProductMultiFilter.as_view()),
]
