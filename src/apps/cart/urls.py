from django.urls import path

from .views import CreateCart, CreateCartItem, DestroyCartItem


urlpatterns = [
    path('', CreateCart.as_view()),
    path('item/', CreateCartItem.as_view()),
    path('item/destroy/<int:id>/', DestroyCartItem.as_view()),
]
