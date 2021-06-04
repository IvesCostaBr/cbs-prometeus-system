from django.shortcuts import render, redirect
from .models import Collaborator
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class CreateCollaborator(CreateView):
    model = Collaborator
    fields = ('nome_completo', 'cpf', 'date_create', 'email')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        
class ListCollaborator(ListView):
    pass
    