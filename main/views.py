from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from shop.models import CurrentItem, FutureItem
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        items = FutureItem.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'main/dashboard.html', context)

    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def dashboard(request):
    items = FutureItem.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'main/dashboard.html', context)


def shop(request):
    """ A view to show all products, including sorting and search queries """

    item_list = CurrentItem.objects.all()
    paginator = Paginator(item_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
        }

    return render(request, 'main/shop.html', context)


def shop_item(request, item_id):
    """ A view to show individual product details """

    item = get_object_or_404(CurrentItem, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'main/shop_item.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            "New Message from" + name,
            message,
            email,
            ['waggyboxmain@gmail.com'],
        )

        return render(request, 'main/contact.html', {"name": name})

    return render(request, 'main/contact.html')
