from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Core.models import *
from Core.models import *
from Core.forms import *


def home(request):
    users=request.user
    Logged_in_user=users.username 
    # if  not users.is_authenticated:
    #         messages.error(request, "Please login to use this Page")
    #         return render(request, 'login.html')
    context = {'user':Logged_in_user , 'usere':users}
    return render(request,'home.html',context=context)


def product_form(request):
    if  not request.user.is_authenticated:
        messages.error(request, "Please login to use this Page")
        return render(request, 'login.html')
    if request.method =='POST':
        name = request.POST.get('prdctname')
        price = request.POST.get('price')
        print(name,price)
        Product_data=product(prdctname=name,price=price)
        Product_data.save()
        return redirect('Homepage')
    return render(request,'product_register.html')


def customer_form(request):
    Products = product.objects.all()
    context = {'products': Products} 
    if  not request.user.is_authenticated:
        messages.error(request, "Please login to use this Page")
        return render(request, 'login.html')
    if request.method == 'POST':
        cus_name = request.POST.get('c_name')
        Purchase = request.POST.get('purchase_product')
        DateOrder = request.POST.get('purchase_date')
        profilepic = request.FILES.get('picture')
        Customer_data = customer.objects.create(c_name=cus_name,Purchase_product=Purchase,Date=DateOrder, profilepic=profilepic)
        print(Customer_data.profilepic)
        return redirect('customerdetails') 
    return render(request, 'customer_register.html', context)


def customer_details(request):
    if  not request.user.is_authenticated:
        messages.error(request, "Please login to use this Page")
        return render(request, 'login.html')
    details = customer.objects.all()
    users = request.user
    print("Request user:", users)
    Logged_in_user = users.username 
    context = {'details': details, 'user': Logged_in_user}
    return render(request, 'customer_details.html', context)

        

def delete(request,id):
    if id:
        person = customer.objects.get(id=id)
        person.delete() 
        return redirect('customerdetails')
    return render(request,'customer_details.html')

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
        person2.profilepic=pic
        person2.save()
        # person2=customer.objects.filter(id=id)
        # person2.update(c_name=name,Date=DateOrder,Purchase_product=Purchase)
        return redirect('customerdetails')
    return render(request, 'update.html',context)

    
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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Homepage')  
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required(login_url='loginuser')
def logouts(request):
    logout(request)
    return redirect('login/')

