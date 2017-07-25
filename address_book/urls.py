from django.conf.urls import url
from . import views

app_name = 'address_book'
urlpatterns = [
    url(r'^$', views.contacts_list_view),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^login/auth$', views.auth_view, name='auth'),
]
