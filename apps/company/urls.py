from django.urls import path
from .views import CreateCompany

urlpatterns = [
    path('create_company/', CreateCompany.as_view(), name='create_company')
]
