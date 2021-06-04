from django.urls import path
from django.urls.conf import include
from .views import Home, Redirect

urlpatterns = [
    path('painel/', Home.as_view(), name='painel'),  
    path('', Redirect.as_view(), name='redirect'), 
    path('comapny/', include('apps.company.urls')),
]
