from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth


def contacts_list_view(request):
    print(request.user)
    if request.user.is_authenticated():
        return render(request, 'address_book/index.html',
                      {'user': request.user})
    else:
        return render(request, 'address_book/err.html')


def login_view(request):
    return render(request, 'address_book/login.html')


def auth_view(request):
    user_name = request.POST['login']
    print(user_name)
    user_password = request.POST['password']
    print(user_password)
    user = auth.authenticate(username=user_name, password=user_password)
    print(user)
    if user is not None:
        auth.login(request, user)

    return HttpResponseRedirect('/')

    # else:
    # return HttpResponseRedirect('address_book/err')
