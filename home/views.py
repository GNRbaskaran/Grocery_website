from django.shortcuts import render,redirect
from .models import UserModel,Product1,Cart,Payment
def home(request):
    return render(request,"index.html")
def signup(request,method=['GET','POST']):
    if request.method=='POST':
        email=request.POST.get('email')
        passw1=request.POST.get('psw')
        passw2=request.POST.get('psw2')
        print(email)
        print(passw1)
        print(passw2)
        UserModel.objects.create(email=email,password=passw1)
        return render(request,'login.html')
    return render(request,'signup.html')
def login(request,method=['GET','POST']):
    if request.method=='POST':
        email=request.POST.get('email')
        passw=request.POST.get('passw')
        ob=UserModel.objects.filter(email=email,password=passw)
        if(ob):
            return redirect("/index/")
        else:
            return render(request,"login.html")
    return render(request,'login.html')
def index(request):
    ob=Product1.objects.all()
    return render(request,"main.html",{"ob":ob})
def main(request,id):
    sum=0
    product=Product1.objects.filter(id=id)
    ob=Cart.objects.filter(product=product[0])
    if(ob):
        ob[0].quantity=ob[0].quantity+1
        ob[0].save()
    else:
        Cart.objects.create(product=product[0],quantity=1)
    all=Cart.objects.all()
    for i in all:
        sum=sum+i.quantity*i.product.price
    return render(request,"cart.html",{"all":all,"sum":sum})
def buy(request):
    x=request.GET.get("x")
    return render(request,"buy.html",{"x":x})
def payment(request,method=['GET','POST']):
    if request.method=='POST':
        name=request.POST.get("cardname")
        cnum=request.POST.get("cardnumber")
        total=request.POST.get("amount")
        Payment.objects.create(name=name,cnum=cnum,total=total)
        Cart.objects.all().delete()
        return render(request,"payment.html")

    return render(request,"payment.html")