from django.shortcuts import render,redirect
from .models import register
from .forms import AddForm
from django.contrib.auth import logout
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.



def insert(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        
        register(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password,gender=gender).save()
    return render(request,'registration.html')


def loginpage(request):
    return render(request,'loginpage.html')

def view(request):
    cr = register.objects.all()
    return render(request,'view.html',{'cr':cr})

def detailview(request,pk):
     cr=register.objects.get(id = pk)
     return render(request,'detailview.html',{'cm':cr})

def update(request,pk):
    cr= register.objects.get(id = pk)
    form=AddForm(instance=cr)
    if request.method == 'POST':
        form=AddForm(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect('view')
    return render(request,'update.html',{'form':form})

def delete(request,pk):
    cr=register.objects.get(id = pk)
    cr.delete()
    return redirect('view')

def userlogin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        cr=register.objects.filter(email=email, password=password)
        if cr:
            user_details=register.objects.get(email=email, password=password)

            id=user_details.id
            firstname=user_details.firstname
            lastname=user_details.lastname
            email=user_details.email

            request.session['id']=id
            request.session['firstname']=firstname
            request.session['lastname']=lastname
            request.session['email']=email

        
            return redirect('display')
        else:
            err="invalid username or password"
            return HttpResponse(render(request,'login.html',{'err':err}))
    else:
        return render(request,'view.html')

def display(request):
    id= request.session['id']
    firstname=request.session['firstname']
    lastname=request.session['lastname']
    return render(request,'display.html',{'id':id,'firstname':firstname,'lastname':lastname})

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def adminlogin(request):
    return render(request,'adminlogin.html')
def alogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')

