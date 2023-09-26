import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import certifi
import ssl
from django.contrib import messages
from django.conf import settings
import uuid
from .models import *
from django.core.mail import send_mail


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
            return redirect('user_desh')
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

                    auth_token = str(uuid.uuid4())
                    pro_obj = Profile.objects.create(user=user, auth_token=auth_token)
                    pro_obj.save()

                    send_mail_reg(Email_address, auth_token)

                    # user.set_password(Password)
                    # user.save()

                    return redirect('success')
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
        if User.objects.filter(email=email):
            messages.warning(request, "Your user Found")
            user = User.objects.get(email=email)

            if Pass == Pass1:
                user.set_password(Pass)
                user.save()
                messages.success(request, "Password reset successful. You can now log in with your new password.")
                return redirect('login')
    return render(request, 'Accounts/reset_pass.html')


def success(request):
    return render(request, 'Accounts/success.html')


def token_send(request):
    return render(request, 'Accounts/token_send.html')


def error(request):
    return render(request, 'Accounts/error.html')


def send_mail_registration(Email, auth_token):
    subject = 'Your Account Authentication Link'
    message = f'hi , Here is the verification link for your account:  http://127.0.0.1:8000/accounts/verify/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    ssl._create_default_https_context = ssl._create_unverified_context

    try:
        with ssl_context:
            send_mail(subject, message, email_from, recipient_list)

    finally:
        ssl._create_default_https_context = ssl._create_default_https_context


def send_mail_reg(Email_address, auth_token):
    subject = 'Your Account Authentication Link'
    message = f'Hi , please click the link to verify your account:  http://127.0.0.1:8000/account/verify/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email_address]
    send_mail(subject, message, email_from, recipient_list)


def verify(request, auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    profile_obj.is_verified = True
    profile_obj.save()
    messages.success(request, 'Congratulation Account verify Its Done')
    return redirect('login')


def user_desh(request):
    return render(request, 'Accounts/user-desh.html')
