from django.shortcuts import render
from .models import Company
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateCompany(LoginRequiredMixin,CreateView):
    model = Company
    fields = ('razao_social',  'cnpj', 
              'endereco', 'cep')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.responsavel = self.request.user
        obj.save()
    

