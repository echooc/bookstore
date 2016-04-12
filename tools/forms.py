#coding:utf-8
from django import forms

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    #repassword = forms.CharField()
    # username = forms.CharField(label='用户名',max_length=100)
    # password = forms.CharField(label='密码',widget=forms.PasswordInput())

class Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()

class ImforFrom(forms.Form):
    bookname = forms.CharField()
    classify = forms.CharField()
    price = forms.CharField()
    discribe = forms.CharField()
    booknumber = forms.CharField()
    picturename = forms.FileField()

# class ImageUploadForm(forms.Form):
#     image = forms.ImageField()

