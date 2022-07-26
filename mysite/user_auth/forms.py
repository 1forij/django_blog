from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
                label='用户名',
                min_length=5,
                error_messages={
                    "required": "用户名不能为空",
                    "min_length": "用户名最短5位",
                },
                widget=forms.TextInput(attrs={"placehold":'5位及以上的用户名','class':'form-control'})
            )
    password = forms.CharField(
                label='密码',
                min_length=6,
                error_messages={
                    "required": "密码不能为空",
                    "min_length": "密码最短6位",
                },
                widget=forms.PasswordInput(attrs={"placehold":'6位及以上的密码','class':'form-control'})
            )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("用户名或密码不正确")
        else:
            self.cleaned_data["user"] = user
        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',
                               min_length=5,
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入5位及以上用户名'})
                            )
    email = forms.EmailField(label='邮箱',
                             widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'请输入邮箱'})
                            )
    password = forms.CharField(label='密码',
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'6位及以上的密码'})
                            )
    password_again = forms.CharField(label='再输入一次密码',
                                     min_length=6,
                                     widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'再输入一次密码'})
                                )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次输入的密码不一致')
        return password_again