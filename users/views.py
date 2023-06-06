from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(requset):
    if requset.method == 'POST':
        form = UserRegisterForm(requset.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(requset , f'Account created for {username}!')
            return redirect('login')
        
    else:
        form = UserRegisterForm()
    return render(requset , 'users/register.html' , {'form':form})

