from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from .models import school_tab


# Create your views here.
def form(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        dob = request.POST.get('dob','')
        age = request.POST.get('age','')
        gender = request.POST.get('gender','')
        phoneno = request.POST.get('phoneno','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        debitnotebook = request.POST.get('debitnotebook','')
        pen = request.POST.get('pen','')
        exampaper = request.POST.get('exampaper','')



        School_tab=school_tab(name=name,dob=dob,age=age,gender=gender,
                                        phoneno=phoneno,email=email,address=address,debitnotebook=debitnotebook,
                                        pen=pen,exampaper=exampaper,)
        School_tab.save();
        if debitnotebook == 'on':
            True
        else:
            False
        messages.info(request,"Order Confirmed")
    return render(request,"form.html")

def login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"newpage.html")
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return render(request,"login.html")
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        pwd = request.POST['pd']
        cpd = request.POST['cpd']
        if pwd==cpd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return render(request,"register.html")
            else:
                user = User.objects.create_user(username=username, password=pwd)
                user.save();
                messages.info(request, "USER REGISTRATION SUCCESSFULL")
                return render(request,"login.html")
        else:
            messages.info(request, "Password Not Matching")
            return render(request,"register.html")
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def newpage(request):
    return render(request,"newpage.html")
def loginbutton(request):
    return render(request,"login.html")
def new(request):
    return render(request,"new.html")