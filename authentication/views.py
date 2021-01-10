from django.shortcuts import render, HttpResponse, redirect
from .models import signUpCode, passwordResetCode
from django.contrib.auth.models import User, auth
import random
from pymongo import MongoClient

con = MongoClient('localhost', 27017)


def index(request):
    user_id = str(request.user)
    database = con.website
    table = database.reviews
    aa = table.find_one({'user_id': user_id})
    return render(request, 'account.html', {'name': aa})


def register(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            code = str(request.POST['code'])
            name = request.POST['name']
            password = request.POST['password']
            find_email = signUpCode.objects.filter(Email=email).first()
            if find_email:
                if find_email.code == code:
                    User.objects.create_user(username=email, password=password, first_name=name).save()
                    user = auth.authenticate(username=email, password=password)
                    auth.login(request, user)
                    return redirect('/account/')
                else:
                    return render(request, 'register_otp.html', {'error': "Check your code"})
            else:
                return redirect('/account/register')
        except:
            try:
                email = request.POST['email']
                if User.objects.filter(username=email).exists():
                    return render(request, 'register.html', {"error": "This Email is taken"})
                else:
                    code_user = random.randint(10000, 99999)
                    print(code_user)
                    email_db = signUpCode.objects.filter(Email=email)
                    if email_db:
                        email_db.update(code=code_user)
                    else:
                        signUpCode(Email=email, code=code_user).save()
                    return render(request, 'register_otp.html')
            except:
                return redirect('/account/register')

    elif request.method == 'GET':
        return render(request, 'register.html')

    else:
        return HttpResponse("Page Not avalable")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/account/')

        else:
            return render(request, 'login.html', {"error": "Login failed wrong user credentials"})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/account/')


def passwordreset(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            code = str(request.POST['code'])
            password = request.POST['password']
            user = passwordResetCode.objects.filter(email=email).first()
            if user.code == code:
                u = User.objects.get(username=email)
                u.set_password(password)
                u.save()
                return redirect('/account/login')
            else:
                return render(request, 'passwordreset_otp.html', {"error" : 'check your code'})
        except:
            try:
                email = request.POST['email']
                if User.objects.filter(username=email).exists():
                    if passwordResetCode.objects.filter(email=email):
                        code_user = random.randint(10000, 99999)
                        print(code_user)
                        passwordResetCode.objects.filter(email=email).update(code=code_user)
                    else:
                        code_user = random.randint(10000, 99999)
                        print(code_user)
                        passwordResetCode(email=email, code=code_user).save()
                    return render(request, 'passwordreset_otp.html')
                else:
                    return render(request, 'passwordreset.html', {'error': "ckeck email"})
            except:
                return redirect('account/passwordreset')

    else:
        return render(request, 'passwordreset.html')
