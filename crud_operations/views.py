from django.http.response import HttpResponse
from database_tables.models import Customer
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.views import generic
# Create your views here.

def getCustomerinfo(request):
    c = {}
    c.update(csrf(request))
    return render(request,'addCustomerinfo.html', c)

def addCustomerinfo(request):
    
    if request.POST.get('submit')=="Enter":
        cName = request.POST.get('customername', '')
        c_aadhharId = request.POST.get('aadhharId')
        c_nomineeName = request.POST.get('nomineeName', '')
        c_income = request.POST.get('income',0)
        c_address = request.POST.get('Address', '')
        c_mobile = request.POST.get('mobile',0)
        c = Customer(customerName = cName,aadhharId = c_aadhharId,nomineeName = c_nomineeName,income = c_income,
        address = c_address,mobile = c_mobile)
        #try:
        c.save()
        return HttpResponseRedirect('/crud_operations/addsuccess/')
        
    else:
        return render(request,'addCustomerinfo.html',{'message':"First,Please enter details!"})

def addsuccess(request):
     return render(request,'addrecord.html')

def viewCustomer(request):
    customer = Customer.objects.all()
    return render(request, 'Customer_list.html', {'customer': customer})

def delCustomerinfo(request):
	aadhaarId = request.POST.get('aadhharId', '')
	customer = Customer.objects.filter(aadhharId = aadhaarId)
	for c in customer:
		c.delete()
	return render(request,'delrecord.html')
