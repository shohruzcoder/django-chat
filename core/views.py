from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignUpForm

# Create your views here.
def frontpage(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    
    context = {
        'form':form
    }
    return render(request, 'signup.html', context)