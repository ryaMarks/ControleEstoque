from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here
def user_login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(login(request, user))
            return redirect('core:index')
        else:
            return render(request, 'login.html')
    return render(request, template_name, {})
