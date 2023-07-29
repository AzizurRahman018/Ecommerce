from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def LOGIN(request):
    return render(request, 'Accounts/login.html')


def Registration(request):
    if request.method == 'POST':
        First_name = request.POST.get('first')
        Last_name = request.POST.get('last')
        user_name = request.POST.get('username')
        Email_address = request.POST.get('email')
        Password = request.POST.get('pass')
        Retype_password = request.POST.get('pass1')
        # if user_name is not None:
        #     if User.objects.filter(username=user_name).exists():
        #         pass
        #     elif User.objects.filter(email=Email_address).exists():
        #         pass
        # else:
        print(First_name,Last_name,user_name,Email_address,Password,Retype_password)
        if Password == Retype_password:
            user = User.objects.create_user(first_name=First_name, last_name=Last_name, username=user_name, email=Email_address, password=Password)
            user.set_password(Password)
            user.save()
            return redirect('login')

    return render(request, 'Accounts/registration.html')
