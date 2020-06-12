from django.shortcuts import render
from django.conf import settings
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

        return render(request, 'main/contact.html', {"name" : name})

    return render(request, 'main/contact.html')