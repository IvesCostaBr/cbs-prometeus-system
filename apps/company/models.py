from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Company(models.Model):
    
    STATUS_COMPANY = {
        (0, 'Inativo'),
        (1, 'Ativo'),
    }
    
    razao_social = models.CharField(max_length=40, 
    help_text="Razão Social da Empresa")
    responsavel = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    cnpj = models.CharField(max_length=18)
    data_cadastro = models.DateField(default=timezone.now)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=14)
    phone = models.CharField(max_length=10, blank=True)
    status = models.BooleanField(default=1, choices=STATUS_COMPANY, blank=True, )
    
    def get_absolute_url(self):
        return reverse('redirect')
    
    def __str__(self):
        return str(self.razao_social) + " " + str(self.cnpj)
