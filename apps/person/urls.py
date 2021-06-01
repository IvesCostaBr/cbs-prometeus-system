from django.urls import path
from .views import (
   CreateClienteData, 
    
)



urlpatterns = [
    path('create_cliente/', CreateClienteData.as_view(), name='create_cliente'),
]
