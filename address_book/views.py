from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def contacts_list_view(request):
    current_user = request.user
    user_contacts = Contact.objects.filter(user_id=current_user.id)
    return render(request, 'address_book/base.html',
                  {'user_contacts': user_contacts})
