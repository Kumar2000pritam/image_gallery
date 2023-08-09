from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from . models import Feedback, Pictures
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            x=User.objects.create_user(username=username,email=email,password=password1)
            x.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'context':"Pleae confirm same passwords"})
    return render(request,'register.html')



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)

        print(user)
        if user is not None:
            request.session['uid']=user.id
            return redirect('imagegallery')
        else:
            return render (request,'login.html',{"context":"check the credentials"})
    return render (request,'login.html')
def logout_view(request):
    del request.session['uid']
    logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'profile.html')


def imagegallery(request):
    if request.session.has_key('uid'):
        user=User.objects.get(id=request.session['uid'])
        if request.method=="POST":
            image=request.POST['image']
            print(user)
            x=Pictures.objects.create(username=user,pic=image)
            x.save()
            return redirect('imagegallery')
    
        all_pictures= Pictures.objects.filter(username=request.session['uid'])
        print(all_pictures)
        a={"all_pictures":all_pictures,'user':user}
        return render(request,'imagegallery.html', a)
    else:
        return redirect('login')
def update_profile(request):
    return render(request,'update_profile.html')

def update_password(request):
    return render(request,'update_password.html')


def feedbacks(request):
    if request.session.has_key('uid'):
        user=User.objects.get(id=request.session['uid'])
        if request.method=="POST":
            feedbacks=request.POST['feedbacks']
            x=Feedback.objects.create(user=user,feedback=feedbacks)
            x.save()
            redirect ('feedbacks')
        return render(request,'feedback.html')
    else:
        return redirect('login')