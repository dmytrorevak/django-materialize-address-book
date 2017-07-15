from django.shortcuts import render
from .models import Contact


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts-list.html', {'contacts': contacts})


def contact_detail(request, contact_name):
    current_contact = Contact.objects.get(name=contact_name)
    return render(request, 'contact-detail.html', {'contact': current_contact})
