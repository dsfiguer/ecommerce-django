from django.urls import path

from .views import GetProduct, ListSiteProducts


urlpatterns = [
    path('list/<str:name>/', ListSiteProducts.as_view()),
    path('get/<str:sku>/', GetProduct.as_view()),
]
