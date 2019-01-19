from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .import forms
from django.http import HttpResponseRedirect
from pratikapp.models import Task






def home(request):
    return render(request,'pratikapp/home.html')


@login_required
def create(request):
    return render(request,'pratikapp/create.html')

@login_required
def retrive(request):
    return render(request,'pratikapp/retrive.html')



def logout(request):
    return render(request,'pratikapp/logout.html')


def Signupform(request):
    form=forms.Userform()
    if request.method=='POST':
        form=forms.Userform(request.POST)
        User=form.save()
        User.set_password(User.password)
        User.save()
        return HttpResponseRedirect('/')
    return render(request,'pratikapp/signup.html',{'form':form})


def create(request):
    form=forms.TaskForm()
    if request.method=='POST':
        form=forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    return render(request,'pratikapp/create.html',{'form':form})


def retrive(request):
    tasklist=Task.objects.all()
    return render(request,'pratikapp/retrive.html',{'tasklist':tasklist})


def delete_view(request,id):
    tasklist=Task.objects.get(id=id)
    tasklist.delete()
    return HttpResponseRedirect('/')

def update_view(request,id):
    tasklist=Task.objects.get(id=id)
    if request.method=='POST':
        form=forms.TaskForm(request.POST,instance=tasklist)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'pratikapp/update_view.html',{'tasklist':tasklist})
