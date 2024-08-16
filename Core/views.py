from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from Core.models import *
from Core.models import *
from Core.forms import *
def errored(request):
    return render(request,'errorpage.html')


def home(request):
    users=request.user
    Logged_in_user=users.username 
    context = {'user':Logged_in_user}
    return render(request,'home.html',context=context)

@login_required(login_url='loginuser')
def product_form(request):
    if request.method =='POST':
        name = request.POST.get('prdctname')
        price = request.POST.get('price')
        print(name,price)
        Product_data=product(prdctname=name,price=price)
        Product_data.save()
        return redirect('Homepage')
    return render(request,'product_register.html')

@login_required(login_url='loginuser')
def customer_form(request):
    Products = product.objects.all()
    context = {'products': Products} 
    if request.method == 'POST':
        cus_name = request.POST.get('c_name')
        Purchase = request.POST.get('purchase_product')
        DateOrder = request.POST.get('purchase_date')
        profilepic = request.FILES.get('picture')
        Customer_data = customer.objects.create(c_name=cus_name,Purchase_product=Purchase,Date=DateOrder, profilepic=profilepic)
        print(Customer_data.profilepic)
        return redirect('customerdetails') 
    return render(request, 'customer_register.html', context)

@login_required(login_url='loginuser')
def customer_details(request):
        details = customer.objects.all()
        users=request.user
        Logged_in_user=users.username 
        context = {'details': details,'user':Logged_in_user}
        return render(request, 'customer_details.html', context)

@login_required(login_url='loginuser')
def delete(request,id):
    print(id)
    if id:
        person = customer.objects.get(id=id)
        person.delete() 
        return redirect('customerdetails')
    return render(request,'customer_details.html')

@login_required(login_url='loginuser')
def update(request,id):
    customers=customer.objects.get(id=id)
    products=product.objects.all()
    context={'customer':customers,'products':products,'id':id}
    if request.method == 'POST':
        name = request.POST.get('c_name')
        Purchase = request.POST.get('purchase_product')
        DateOrder = request.POST.get('purchase_date')
        pic = request.FILES.get('picture')
        person2=customer.objects.get(id=id)
        person2.c_name=name
        person2.Date=DateOrder
        person2.Purchase_product=Purchase
        person2.save()
        # person2=customer.objects.filter(id=id)
        # person2.update(c_name=name,Date=DateOrder,Purchase_product=Purchase)
        return redirect('customerdetails')
    return render(request, 'update.html',context)

@login_required(login_url='loginuser')
def formUser(request):
    form=addtsudentForm()
    if request.method == 'POST':
        fromdata=addtsudentForm(request.POST)
        if fromdata.is_valid():
            form.save()
            return redirect('Homepage')
    context={
        'form':form
    }
    return render(request,'form.html',context=context)
    

def register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        Fpassword=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        # password=confirm_password
        # data=account.objects.create(username=username,password=password)
        # data.save()
        password=confirm_password
        data=User.objects.create(username=username)
        data.set_password(confirm_password)
        data.save()
    return render(request,"login.html")


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('Lusername')
        password = request.POST.get('Lpassword')
        user = authenticate( username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('Homepage')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required(login_url='loginuser')
def logouts(request):
    logout(request)
    return redirect('login/')

