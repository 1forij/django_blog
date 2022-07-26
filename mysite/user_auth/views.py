from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login, logout, authenticate
from user_auth.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
def to_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request, user)
            return redirect(request.GET.get('from', '/'))
    else:
        login_form = LoginForm()

    return render(request, 'user_auth/user_login.html', {'login_form':login_form})

@login_required(login_url='/user_auth/login')
def to_logout(request):
    logout(request)
    return JsonResponse({'status':'SUCCESS'})    #  ajax  jquery解决

def to_register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password"]
            email = register_form.cleaned_data['email']
            # 创建用户
            User.objects.create_user(username=username,email=email,password=password)
            # 登录
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return redirect(request.GET.get('from', '/'))
    else:
        register_form = RegisterForm()

    return render(request, 'user_auth/user_register.html', {'register_form':register_form})


# class To_login(View):
#     url_previous = ''
#
#     def get(self, request):
#         login_form = LoginForm()
#         To_login.url_previous = request.GET.get("from",'')
#         return render(request,'user_auth/user_login.html',{'login_form':login_form})
#
#     def post(self, request):
#         # 把post传过来的数据经由LoginForm验证处理，并且实例出一个对象
#         login_form = LoginForm(request.POST)
#
#         if login_form.is_valid():       # is_valid：有效且合法的数据（并且通过了clean函数）
#             user = login_form.cleaned_data["user"]   # 取出通过auth的user
#             login(request, user)
#             return redirect(self.url_previous or '/')   # 返回重定向为原博客或者主页 reverse(home)也行
#         else:
#             return render(request, 'user_auth/user_login.html', {'login_form': login_form})
