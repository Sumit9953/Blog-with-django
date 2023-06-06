from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request):
    return render(request , 'users/profile.html' )