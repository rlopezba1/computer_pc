from django.shortcuts import render
from .models import FAQ

# Create your views here.


def view_contact(request):
    """ Return contact page """
    context = {
        'active_page': 'contact',
    }

    return render(request, 'contact.html', context)


def view_faqs(request):
    """ Return faqs page """

    questions = FAQ.objects.all()

    context = {
        'questions': questions,
    }

    return render(request, 'faqs.html', context) 


def view_about(request):
    """ Return about page """
    context = {
        'active_page': 'about',
    }

    return render(request, 'about.html', context) 