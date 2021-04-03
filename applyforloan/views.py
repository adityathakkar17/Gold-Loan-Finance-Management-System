from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer, GoldAsset, LoanApplication, LoanRates, Payment
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.models import User
from math import pow

# Create your views here.
def applyForLoan(request):
    rate = LoanRates.objects.last()
    return render(request,'index.html',{"goldvalue":rate.GoldValue,"interest":rate.RateOfInterest,"ltv":rate.ltvRatio})

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
            user = User.objects.create_user(username = username, password = password)
            user.save()
            goldtype = request.POST.get('goldtype')
            weight = request.POST.get('goldweight')
            customerId = c.customerId
            g = GoldAsset(goldtype=goldtype,weight=weight,customerId_id=customerId)
            g.save()
            rate = LoanRates.objects.last()
            if rate is None:
                loanrate = LoanRates()
                loanrate.save()
                rate = LoanRates.objects.last()
            goldvalue = int(rate.GoldValue/10)
            interest = float(rate.RateOfInterest)
            loanamount = goldvalue * int(weight) 
            tenure = int(request.POST.get('tenure'))
            assetId = g.assetID
            t = tenure*12
            r = interest/(12*100)
            emi = int(loanamount * r * pow((1+r),t)/(pow((1+r),t)-1))
            print(emi)
            totalLoanAmount = emi*t
            l = LoanApplication(principalAmount = loanamount,lentLoanTenure = tenure,lentGoldValue=rate.GoldValue,lentRateOfInterest=rate.RateOfInterest,lentltvRatio=rate.ltvRatio,
            totalLoanAmount = totalLoanAmount,emi=emi,customerId_id = customerId,assetId_id = assetId)
            l.save()
            cardtype = request.POST.get('cardtype')
            cardnumber = request.POST.get('cardnumber')
            cvc = request.POST.get('cvc')
            expmonth = request.POST.get('expmonth')
            expyear = request.POST.get('expyear')
            p = Payment(cardtype = cardtype,cardnumber = cardnumber,cvc = cvc,expmonth =  expmonth,expyear = expyear,customerId_id = customerId)
            p.save()
        except:
            messages.error(request,"Please enter proper details")
            return HttpResponseRedirect('/applyforloan/apply')
        messages.success(request,"Application submitted successfully!!")
        messages.success(request,"Login with your username and passsword.")
        return HttpResponseRedirect('/loginmodule/login')
    else:
        messages.error(request,"Please enter proper details")
        return HttpResponseRedirect('/applyforloan/apply')



