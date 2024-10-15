from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from cart.models import Product
from django.db.models import Q

#Q means query
def home(request):
    # userid = request.user.id
    # #print(userid)
    # print(request.user.is_authenticated)
    # return render(request,'index.html')
    context ={}
    p = Product.objects.filter(is_active=True)
    context['products'] = p
    return render(request,'index.html', context)

def product_details(request):
    return render(request,'product_details.html')
def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        context= {}
        if uname == "" or upass == "" or ucpass == "":
            context['errmsg']="Fileds cannot be empty"
        elif upass != ucpass:
            context['errmsg']="Password & confirm password didnot match"
        else:
            try:
                u = User.objects.create(username=uname, password=upass, email=uname )
                u.set_password(upass)
                u.save()
                context['success'] = "user  created successfully ,please login"
            except Exception:    
                context['errmsg'] = "user  with same username already exist!!"
        
        #return HttpResponse("user created successfully")
        return render(request,'register.html',context)

    else:
        return render(request,'register.html')

    

def contact(request):
    return render(request,'contact.html')



def about(request):
    return render(request,'about.html')

def user_login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        print(uname,upass)
        if uname =='' or upass == '':
            context['errmsg']='Fields are empty'
            return render(request,'login.html',context)
        else:
            user = authenticate(request,username=uname,password=upass)
            # print(user.password, user.is_superuser)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                context['errmsg'] = "Invalid username and password"
                return render(request,'login.html',context)
                
        
    else:
        return render(request,'login.html')
        return HttpResponse("data fetched")
# Create your views here.
def user_logout(request):
    logout(request)
    return redirect('/home')

def catfilter(request, cv):
    q1=Q(is_active=True)
    q2=Q(cat=cv)
    p =Product.objects.filter(q1 & q2)
    # print(p)
    context ={}
    context['products'] = p
    return render(request,'index.html',context)

def sort(request, sw):
    if sw == '0':
        col = 'price' #low to high
        
    else:
        col = '-price' #high to low
    # p = Product.objects.order_by(col)  
    p = Product.objects.filter(is_active=True).order_by(col)   

    context ={}
    context['products'] = p
    return render(request,'index.html',context)    

def range(request):
    min = request.GET['min']
    max = request.GET['max']
    print(min, max)
    return HttpResponse("Data Fetched")


