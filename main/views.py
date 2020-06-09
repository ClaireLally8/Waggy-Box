from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'main/dashboard.html')

    return render(request, 'main/index.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')