from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'main/dashboard.html')

    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def dashboard(request):
    return render(request, 'main/dashboard.html')


def shop(request):
    return render(request, 'main/shop.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # send an email 
        send_mail(
            "New Message from" + name , #subject
            message, #message itself
            email, #from email address
            ['waggyboxmain@gmail.com'], #to email address
        )

        return render(request, 'main/contact.html', {"name" : name})

    return render(request, 'main/contact.html')