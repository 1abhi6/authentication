from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password1 = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        #     print(
        #         f"{username}, {firstName}, {lastName}, {email}, {password}, {confirmPassword}")
        # return render(request, "signup.html")

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstName
        myuser.last_name = lastName

        myuser.save()

        print("Success")
        messages.success(request, "Your account has been succesfully created.")
        return redirect(request,"login")

    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")
