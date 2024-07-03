# views.py
from django.shortcuts import render, redirect
from .form import RegistrationForm
from django.contrib import messages

def registration(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  
    else:
        fm = RegistrationForm()
    return render(request, 'registration.html', {'fm': fm})
