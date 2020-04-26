from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import auth
from django.views.generic.edit import CreateView
from .models import BaraUser

# Create your views here.


def index(request):
    pass


class UserLoginView(CreateView):

    template_name = 'authapp/sign.html'
    model = BaraUser
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pagemode'] = pagemode
    #     return context
    