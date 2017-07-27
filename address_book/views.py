from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def contacts_list_view(request):
    # print(request.user)
    # if request.user.is_authenticated():
    #     return render(request, 'address_book/index.html',
    #                   {'user': request.user})
    # else:
    #     return render(request, 'address_book/err.html')
    return render(request, 'address_book/base.html', {'user': request.user})
