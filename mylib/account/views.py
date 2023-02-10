from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from  django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import ListView

class List(ListView):
    model = MyUser
class Loginview(View):
    def get(self,r):
        return render(r, 'Login.html')
    def post(self,r):
        user = MyUser.objects.filter(username=r.POST['username'], password=r.POST['password'])
        authuser = authenticate(username=r.POST['username'], password=r.POST['password'])
        print(authuser)
        if (user[0] is not None and authuser is not None):
            req.session['userid'] = user[0].id
            req.session['username'] = user[0].username
            login(r, authuser)
            return HttpResponseRedirect('/')
        else:
            context = {}
            context['error'] = 'username or password is wrong'
            return render(r, 'Login.html', context)


@require_http_methods(['GET'])

def mylogin(r):
    return render(r,'Login.html')
def mylogout(r):
    req.session.clear()
    return HttpResponseRedirect('Login')
def myregister(r):
    if(req.method=='GET'):
        return render(r,'Register.html')
    else:
        reg=MyUser.objects.create(username=r.POST['username'],password=r.POST['password'])
        User.objects.create_user(username=r.POST['username'],password=r.POST['password'],email='rania@yahoo.com')
        req.session['userid']=reg.id
        req.session['username']=reg.username
        return HttpResponseRedirect('/')

def mylogin2(r):
    if (r.method == 'GET'):
        return render(r, 'Login.html')
    else:
        user = MyUser.objects.filter(username=r.POST['username'], password=r.POST['password'])
        authuser=authenticate(username=r.POST['username'],password=r.POST['password'])
        print(authuser)
        if (user[0] is not None and authuser is not None):
            req.session['userid'] = user[0].id
            req.session['username'] = user[0].username
            login(r,authuser)
            return HttpResponseRedirect('/')
        else:
            context = {}
            context['error'] = 'username or password is wrong'
            return render(req, 'Login.html', context)


def myregister2(r):
    if(r.method=='POST'):
        reg=MyUser.objects.create(
            username=r.POST['username'],
            password=r.POST['password'],
            email=r.POST['email']
        )
        User.objects.create_superuser(username=r.POST['username']
                                      , password=r.POST['password'],
                                      email=r.POST['email'])

        r.session['userid']=reg.id
        r.session['username']=reg.username

        return  render(r,'Book/index.html')
    else:
        return render(r, 'Register.html' )
def mylogout2(r):
    r.session.clear()
    return HttpResponseRedirect('Login')

