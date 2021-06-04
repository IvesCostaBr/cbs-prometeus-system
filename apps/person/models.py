from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nome_completo = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    date_create = models.DateField(default=timezone.now)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.nome_completo)


