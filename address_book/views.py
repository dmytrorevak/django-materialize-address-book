from django.shortcuts import render


def contacts_list_view(request):

    if request.user.is_authenticated():
        return render(request, 'address_book/index.html',
                      {'user': request.user})
    else:
        return render(request, 'address_book/err.html')
