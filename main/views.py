from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from shop.models import CurrentItem, FutureItem
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from memberships.models import UserMembership, Subscription
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


@login_required()
def get_user_membership(request):
    """ 
    This view renders the logged in users membership type.  
    Required in this view to limit the user access to certain pages. 
    """
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


@login_required()
def get_user_subscription(request):
    """ 
    This view renders the logged in users subscription.  
    Required in this view to limit the user access to certain pages. 
    """
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def index(request):
    """ 
    Renders the index page if the user is not logged in & 
    renders the dashboard if the user is logged in.
    """
    if request.user.is_authenticated:
        return redirect(dashboard)

    return render(request, 'main/index.html')


def about(request):
    """
    Renders the about html page.
    """
    return render(request, 'main/about.html')


@login_required()
def dashboard(request):
    """ 
    This function renders the dashboard page. Returning the users subscription and the items which are next months items. 
    """
    subscription = get_user_subscription(request)
    items = FutureItem.objects.all()
    context = {
        'items': items,
        'subscription': subscription,
    }
    return render(request, 'main/dashboard.html', context)


@login_required()
def shop(request):
    """ A view to show all products. Also returns items on a page, which is limited to 12 items per page. 
    Checks if the user has a subscription and if this is active.
    If no for both, it will return the no auth page, otherwise it will return the shop page. """
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
    """ A view to show indivdual shop items. Checks if the user has a subscription and if this is active.
    If no for both, it will return the no auth page, otherwise it will return the shop page. """

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
        if user_form.is_valid(): # If the form submitted is vaid, an email will be sent. 
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST['email'],
                ['waggyboxmain@gmail.com', request.POST['email']],
                fail_silently=False,
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                'Contact form sent successfully!')
            return redirect('contact')

    user_form = ContactForm()

    context = {
        'user_form': user_form,
    }
    return render(request, 'main/contact.html', context)
