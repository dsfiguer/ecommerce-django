from django.urls import path

from .views import ListSiteProducts


urlpatterns = [
    path('list/<str:name>/', ListSiteProducts.as_view()),
]
