from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(requset):
    if requset.method == 'POST':
        form = UserCreationForm(requset.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(requset , f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(requset , 'users/register.html' , {'form':form})
