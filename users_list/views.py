from django.shortcuts import render
from .models import Contact


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})
