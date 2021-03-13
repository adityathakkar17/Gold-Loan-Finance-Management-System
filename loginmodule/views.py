from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages
from applyforloan.models import Customer, GoldAsset, LoanApplication
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token

def home(request):
    return render(request,"home.html")

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html', c)

def auth_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        # customers = Customer.objects.all()
        # flag = 0
        # for c in customers:
        #     if c.username == username and c.password == password:
        #         flag = 1
        #         asset = GoldAsset.objects.get(customerId_id = c.customerId)
        #         application = LoanApplication.objects.get(customerId_id = c.customerId)
        #         return render(request,"loggedin.html",{"c":c,"a":asset,"appl":application})
        # if flag == 0:
        #     error =" Invalid username or password"
        #     messages.error(request,error)
        #     return HttpResponseRedirect('/loginmodule/login/')

        if user is not None:
            c = Customer.objects.get(username = user.get_username())
            asset = GoldAsset.objects.get(customerId_id = c.customerId)
            application = LoanApplication.objects.get(customerId_id = c.customerId)
            auth.login(request, user)
            return render(request,"loggedin.html",{"c":c,"a":asset,"appl":application})
        else:
            messages.success(request,"Invalid username or password")
            return render(request,'login.html')
            
    return redirect('/loginmodule/login')

@login_required(login_url='/loginmodule/login')
def loggedin(request):
    return render(request,'loggedin.html', {"full_name":request.user.username})

def logout(request):
    auth.logout(request)
    messages.info(request,"Logged out successfully..")
    return render(request,'login.html')