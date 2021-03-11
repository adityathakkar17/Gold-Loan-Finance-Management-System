from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages
from applyforloan.models import Customer
def home(request):
    return render(request,"home.html")

# def about(request):
#     return render(request,"about.html")

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html', c)

def auth_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # user = auth.authenticate(username=username,password=password)
        customers = Customer.objects.all()
        flag = 0
        for c in customers:
            if c.username == username and c.password == password:
                flag = 1
                return render(request,"loggedin.html",{"full_name":c.customerName})
        if flag == 0:
            error =" Invalid username or password"
            messages.error(request,error)
            return HttpResponseRedirect('/loginmodule/login/')

        # if user is not None:
        #     auth.login(request, user)
        #     return HttpResponseRedirect('/loginmodule/loggedin/')
        # else:
        #     messages.success(request,"Invalid username or password")
        #     return HttpResponseRedirect('/loginmodule/login/')

def loggedin(request):
    return render(request,'loggedin.html', {"full_name":request.user.username})

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')