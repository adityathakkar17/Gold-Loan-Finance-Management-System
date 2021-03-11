from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.
def applyForLoan(request):
    return render(request,'index.html')

def addCustomer(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        customerName = request.POST.get('customerName')
        aadhaarId = request.POST.get('aadhaarId')
        nomineeName = request.POST.get('nomineeName')
        income = request.POST.get('income')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('dob')
        c = Customer(username=username,password = password,customerName = customerName,aadhaarId = aadhaarId,nomineeName = nomineeName,
        income = income,address = address,mobile = mobile,dob=dob)
        try:
            c.save()
            # return render(request,"success.html")
            messages.success(request,"Application submitted successfully!!")
            messages.success(request,"Login with your username and passsword.")
            return HttpResponseRedirect('/loginmodule/login')
        except:
            messages.error(request,"Please enter proper details")
            return render(request,'index.html')
            # return render(request,"fail.html",{"error":"Please enter proper details"})
    else:
        return render(request,"fail.html",{"message":"First , Please  fill  the details"})

