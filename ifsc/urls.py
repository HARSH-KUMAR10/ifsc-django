from django.urls import path
from . import views

urlpatterns = [
    path('',views.ifsc_home),
    path('find',views.ifsc_find)
]