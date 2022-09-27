from django.urls import path

from .views import ListSiteProducts


urlpatterns = [
    path('<str:name>/', ListSiteProducts.as_view())
]
