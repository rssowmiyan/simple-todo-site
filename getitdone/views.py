from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import  auth,User
from django.contrib import messages
from django.http import  HttpResponse
from django.contrib.auth import login,logout
from .forms import GetitdoneForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Getitdone
from django.utils import timezone
from django.contrib.auth.decorators import login_required
############################################################################

def home(request):
    return render(request,'home.html')

def register(request):
    if(request.method=='POST'):
        fullname=request.POST['fullname']
        email=request.POST['email']
        username=request.POST['username']
        pwd1=request.POST['password1']
        pwd2=request.POST['password2']
        if(pwd1==pwd2):
            if(User.objects.filter(username=username).exists()):
                messages.error(request,'username exists')
                return redirect('register')

            elif(User.objects.filter(email=email).exists()):
                messages.error(request,'email is already used')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=pwd1,email=email)
                user.save()
                login(request,user)
        else:
            messages.error(request,'password not matching')
            return redirect('register')
        return redirect(currenttodos)

    else:
        return render(request,'signup.html')

@login_required
def currenttodos(request):
    todos=Getitdone.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request,'currenttodos.html',{'todos':todos})

@login_required
def completedtodos(request):
    todos=Getitdone.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request,'completedtodos.html',{'todos':todos})


@login_required
def createtodo(request):
    if(request.method=='GET'):
        return render(request,'createtodo.html',{'form':GetitdoneForm()})
    else:
        try:
            form=GetitdoneForm(request.POST)
            newtodo=form.save(commit=False)
            newtodo.user=request.user
            newtodo.save() 
            return redirect('currenttodos')
        except ValueError:
            return render(request,'createtodo.html',{'form':GetitdoneForm(),'error':'bad data passed in Try again'})
        
@login_required
def logoutuser(request):
    if(request.method=='POST'):
        auth.logout(request)
        return redirect('home')


def loginuser(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request,user)
            return redirect(currenttodos)
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('loginuser')
    else:
        return render(request,'login.html')

@login_required 
def viewtodo(request,todo_pk):
    todo=get_object_or_404(Getitdone,pk=todo_pk,user=request.user)
    if(request.method=='GET'):
        form=GetitdoneForm(instance=todo)
        return render(request,'viewtodo.html',{'todo':todo,'form':form})
    else:
        try:
            # for 'instance =' give 'todo', not the name of the model 'Getitdone'
            form=GetitdoneForm(request.POST,instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request,'viewtodo.html',{'todo':todo,'form':form,'error':'bad value passed in'})

@login_required
def completetodo(request,todo_pk):
    todo=get_object_or_404(Getitdone,pk=todo_pk,user=request.user)
    if(request.method=='POST'):
        todo.datecompleted=timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required
def deletetodo(request,todo_pk):
    todo=get_object_or_404(Getitdone,pk=todo_pk,user=request.user)
    if(request.method=='POST'):
        todo.delete()
        return redirect('currenttodos')

    