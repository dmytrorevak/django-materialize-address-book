from django.conf.urls import url
from . import views

app_name = 'address_book'
urlpatterns = [
    url(r'^$', views.contacts_list_view),
]
