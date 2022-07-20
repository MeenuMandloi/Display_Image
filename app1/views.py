from django.shortcuts import render, redirect
from app1.models import Usertable
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.urls import reverse

def index(request):
    return render(request, "index.html")

def Register(request):
    if request.method == "POST":

        email = request.POST.get('email')
        if Usertable.objects.filter(email=email).exists():
            return HttpResponse("User Already Registered")
        else:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            gender_selection = request.POST.get('gender_selection')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            email = request.POST.get('email')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            # photo = request.FILES.get('filename')
            photo = request.FILES['filename']
            user = Usertable.objects.create(firstname=firstname, lastname=lastname, gender=gender_selection,
                                            phone=phone, address=address, email=email, password=password, photo=photo)
            if user:
                if password != repassword:
                    return HttpResponse("Password does not match")
                else:
                    return render(request, "login.html", {"user": user,'photo': photo})
    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        super_user = User.objects.filter(email=email)
        user = authenticate(request, email=email, password=password)
        check_user = Usertable.objects.filter(email=email)
        if check_user:
            for data in check_user:
                if data.email == email:
                    if data.password == password:
                        request.session['email'] = email
                        user = Usertable.objects.get(email=email)
                        context = {'user': user}
                        return render(request, "myprofile.html", context)
                    else:
                        return HttpResponse('Please enter valid Password.')
                else:
                    return HttpResponse('Please enter valid email.')

    return render(request, 'login.html')
