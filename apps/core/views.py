from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View





class Home(LoginRequiredMixin ,TemplateView):
    template_name = 'core/painel_admin.html'

class Redirect(View):
    def get(self, request, *args, **kwargs):
        try:
            self.request.user.company
            return redirect('painel')
        except:
            return redirect('create_company')