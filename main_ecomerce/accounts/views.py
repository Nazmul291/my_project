from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# register section
def account_register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists')
                return redirect('account_register')

            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('account_register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password=password)
                user.save()
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')

        else:
            messages.info(request, 'password not match')
            return redirect('account_register')

    else:
        user = User.objects.all()
        return render(request, 'accounts/register.html', {'user': user})


# login section o f user
def account_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.filter(username=username) or User.objects.filter(email=username) or User.objects.filter(
            id=username)
        if user.exists():
            for j in user:
                username = j.username
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'username or password invalid')
                    return redirect('account_login')
        else:
            messages.info(request, "user doesn't exist")
            return redirect('account_register')

    else:
        return render(request, 'accounts/login.html')


# logout section
def account_logout(request):
    auth.logout(request)
    return redirect('/')
