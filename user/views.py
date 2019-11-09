from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('') 
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password'] == request.POST['checkpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'}) 
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)

                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')
    return render(request, 'login.html')