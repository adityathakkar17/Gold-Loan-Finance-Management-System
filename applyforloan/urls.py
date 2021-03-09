from django.urls import path
from applyforloan.views import applyForLoan
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url('', applyForLoan),
    url(r'^calc/', TemplateView.as_view(template_name="cal.html"),
                   name='calc'),
]