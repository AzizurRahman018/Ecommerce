from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def LOGIN(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        Password = request.POST.get('password')
        if len(Password) == 0:
            messages.warning(request, "No password Found")
            return redirect('login')

        user = authenticate(username=user_name, password=Password)
        if user:
            login(request, user)
            return redirect('home')
        if Password != User.password:
            messages.warning(request, "your password is incorect")
            return redirect('login')
        # print(user)
        # print('your user name is ',user_name)
    return render(request, 'Accounts/login.html')


def Registration(request):
    if request.method == 'POST':
        First_name = request.POST.get('first')
        Last_name = request.POST.get('last')
        user_name = request.POST.get('username')
        Email_address = request.POST.get('email')
        Password = request.POST.get('pass')
        Retype_password = request.POST.get('pass1')
        if user_name is not None:
            for i in user_name:
                if i == '@' or i == '.' or i == '/':
                    messages.warning(request, "Your username has special charecter ,please remove ")
                    return redirect('registration')
            if User.objects.filter(username=user_name).exists():
                messages.warning(request, "Your user name is already taken !")
            elif User.objects.filter(email=Email_address).exists():
                messages.warning(request, "Your Email is already taken !")
            else:
                print(First_name, Last_name, user_name, Email_address, Password, Retype_password)
                if Password == Retype_password:
                    user = User.objects.create_user(first_name=First_name, last_name=Last_name, username=user_name,
                                                    email=Email_address, password=Password)
                    user.set_password(Password)
                    user.save()
                else:
                    messages.warning(request, "Your Email is already taken !")
            return redirect('login')

    return render(request, 'Accounts/registration.html')


def LOGOUT(request):
    logout(request)
    messages.warning(request, "you are logout")
    return redirect('login')


def RESET_PASS(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            Pass = request.POST.get('password')
            Pass1 = request.POST.get('password1')
            # if User.objects.filter(username=user_name).exists():
            if User.objects.filter(email=email) :
                messages.warning(request, "Your user Found")
                user = User.objects.get(email=email)

                if Pass == Pass1:
                    user.set_password(Pass)
                    user.save()
                    messages.success(request, "Password reset successful. You can now log in with your new password.")
                    return redirect('login')
    return render(request, 'Accounts/reset_pass.html')
