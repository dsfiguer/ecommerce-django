from django.urls import path

from .views import ContactForm


urlpatterns = [
    path('', ContactForm.as_view()),
]
