from django.shortcuts import render
from .models import Company
from django.views.generic.edit import CreateView


class CreateCompany(CreateView):
    model = Company
    fields = ('razao_social',  'cnpj', 
              'endereco', 'cep')

    
    def form_valid(self, form):
        obj = form.save(commit=False)
        print('1231231231')
        obj.responsavel = self.request.user
        obj.save()
    

