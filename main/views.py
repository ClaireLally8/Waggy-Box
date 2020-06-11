from django.shortcuts import render

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
