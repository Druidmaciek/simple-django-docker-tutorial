from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactRequestView.as_view(), name='home')
]
