from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
# path('', views.index, name='index'),
url(r'^addCustomerinfo/$', views.addCustomerinfo),
url(r'^getCustomerinfo/$', views.getCustomerinfo),
url(r'^addsuccess/$', views.addsuccess),
url('viewCustomerinfo/',views.viewCustomer),
url(r'^delCustomerinfo/$', views.delCustomerinfo),
# url('customers/', views.CustomerListView.as_view(), name ='customers'),
]