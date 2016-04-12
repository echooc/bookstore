#coding:utf-8
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from accounts.models import User


# Create your views here.
from django.shortcuts import render

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

def index(request):
    return render(request, 'index.html')

def register(request):
    # if req.method == 'POST':
    #     uf = UserForm(req.POST)
    #     if uf.is_valid():
    #         username = req.GET.get('Username')
    #         password = req.GET.get('Password')
    #         user = User()
    #         user.username = username
    #         user.password = password
    #         user.save()
            return render(request, '../../templates/../accounts/templates/../templates/../templates/login.html')

            #return render_to_response('login.html', {'username': username})
            # User.objects.create(username=username,password=password)
        # else:
        #     uf = User()
        #     return render(req, '../templates/login.html')
       # return render_to_response(login.html', {'uf': uf})
 #def index(request):
     #return render_to_response('index.html', {}, context_instance=RequestContext(request))
