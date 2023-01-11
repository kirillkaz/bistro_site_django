from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from login.forms import CustomAuthForm
from login.models import User
from main_app.forms import DishForm

class UserCreateView(LoginView):
    template_name = 'page.html'
    form_class = CustomAuthForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
    
    def get_success_url(self):
        #return HttpResponse('success login!')
        return reverse_lazy('main_page')


@csrf_exempt
def show(request):
    form = DishForm
    context = {'form': form}
    return render(request, 'testpage.html', context)

@csrf_exempt
def showpage(request):
    form = UserCreateView
    context = {'form': form}
    return render(request, 'page.html', context)
