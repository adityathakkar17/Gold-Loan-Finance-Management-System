from django.urls import path
from loginmodule.views import approve, loggedin_customer, loggedin_admin, login, auth_view, logout,home, reject, update_rates ,pay_emi
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout),
    url(r'^loggedin_admin/$', loggedin_admin),
    url(r'^loggedin_customer/$', loggedin_customer),
    url("home/",home),
    url(r'^update_rates/$',update_rates),
    url(r'^approve/$', approve),
    url(r'^reject/$', reject),
    url(r'^pay_emi/$', pay_emi),
]