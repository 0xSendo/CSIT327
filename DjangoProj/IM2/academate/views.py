from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect

from .forms import *

# Create your views here.


def render_home(request):
    return render(request, 'home.html')

@csrf_protect
def render_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form' : form})