from django.urls import path
from Home.views import *
urlpatterns = [
    path('', home, name='home'),
     path('product_details/<int:id>', product_details, name='product_details'),
]