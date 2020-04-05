from django.shortcuts import render,redirect
#rom django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created Successfully! You can Login now.')
            return redirect('login') 
    else:
         form = UserRegisterForm()
    return render (request,'users/register.html',{'form':form})

@login_required     
def profile(request):
    return render(request,'users/profile.html')
