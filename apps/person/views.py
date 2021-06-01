from django.shortcuts import render, redirect
from .models import ClienteDados
from django.views.generic.edit import CreateView

class CreateClienteData(CreateView):
    model = ClienteDados
    fields = ('nome_completo', 'cpf', 'date_create', 'email')

    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        
    
    