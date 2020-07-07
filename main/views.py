from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from shop.models import CurrentItem, FutureItem
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from memberships.models import UserMembership, Subscription
from .forms import ContactForm
# Create your views here.

@login_required()
def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


@login_required()
def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def index(request):
    if request.user.is_authenticated:
        return redirect(dashboard)

    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


@login_required()
def dashboard(request):
    subscription = get_user_subscription(request)
    items = FutureItem.objects.all()
    context = {
        'items': items,
        'subscription': subscription,
    }
    return render(request, 'main/dashboard.html', context)


@login_required()
def shop(request):
    """ A view to show all products, including sorting and search queries """
    subscription = get_user_subscription(request)
    if subscription:
        if subscription.active:
            item_list = CurrentItem.objects.all()
            paginator = Paginator(item_list, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'page_obj': page_obj
            }

            return render(request, 'main/shop.html', context)

        return render(request, 'main/no_auth.html')

    return render(request, 'main/no_auth.html')

@login_required()
def shop_item(request, item_id):
    """ A view to show individual product details """
    subscription = get_user_subscription(request)
    if subscription:
        if subscription.active:
            item = get_object_or_404(CurrentItem, pk=item_id)

            context = {
                'item': item,
            }

            return render(request, 'main/shop_item.html', context)

            return render(request, 'main/no_auth.html')

    return render(request, 'main/no_auth.html')


def contact(request):
    """A view that allows the user to send and email message redirects back to the contact page"""
    if request.method == 'POST':  # If the form has been submitted...
        user_form = ContactForm(request.POST)  # A form bound to the POST data
        if user_form.is_valid():
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST['email'],
                ['waggyboxmain@gmail.com', request.POST['email']],
                fail_silently=False,
            )

            return redirect(reverse('contact'))

    user_form = ContactForm()

    context = {
            'user_form': user_form,
        }
    return render(request, 'main/contact.html', context)

