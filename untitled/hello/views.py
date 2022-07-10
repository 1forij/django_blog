from django.shortcuts import render
from django.http import HttpResponse

# 导入 对(类)方法进行装饰的装饰器
from django.utils.decorators import method_decorator

# 导入自定义类视图的父类View
from django.views import View

# 导入settings.py内的SECRET_KEY （为了加盐。）
from untitled.settings import SECRET_KEY

# 在session data的测试中用了一下。
from time import ctime

#####################################
# 忘了测试用的。。
def sayhello(request):
    return HttpResponse("hello world")
# 忘了测试用的。。
def var_uid(request):
    head = request.headers
    return HttpResponse(head)
#####################################

# 定义闭包函数作为装饰器执行的函数
def switch(func):                   # 选则过滤。。。（我这个自定义闭包做装饰器功能鸡肋的很。。。）

    def way(request):
        if request.method=='GET':               # 若是GET请求，控制台打印一串字符。。。。。
            print("这是个GET请求，请注意查收处理")
        elif request.method=='POST':            # 若是POST请求，控制台打印一串字符。。。。。
            print("这是个GET请求，请注意查收处理")

        return func(request)
    return way

# 加装饰器后的类视图（为类中每个函数都加上了装饰器）
@method_decorator(switch,name='dispatch')# name的取值'dispatch'(全选), 'get'(仅get), 'post', 'put', 'delete', 'options'等
class Things(View):
    def get(self,request):
        return HttpResponse("this is GET")
    def post(self,request):
        return HttpResponse("this is post")


# 该函数用于cookie的配置
def give_cookie(request):
    d={
        'id':'123',
        'name':'Kali',
        'sex':'man',
        'like':'ball',
    }
    # 实例化响应类的对象
    response = HttpResponse()
    # 基于对象设置cookie
    response.set_cookie(key='name',value='Kali',max_age=60,httponly=True,)
    response.set_cookie(key='data',value=d,expires=80,httponly=True)
    response.set_signed_cookie(key="student_id",value="11452",max_age=60,salt=SECRET_KEY)
    response.set_signed_cookie(key="DIY_id",value="112",max_age=60,salt="haha_faker_salt")

    response.content="内容什么都没有"

    return response


# 该函数读取cookie内容
def read_cookie(request):
    your_name = request.COOKIES.get('name')
    your_data = request.COOKIES.get('data')

    your_info = your_name+your_data

    return HttpResponse(your_info)

# 该函数删除cookie
def remove_cookie(request):
    response = HttpResponse()

    response.delete_cookie("name")

    return response

# 该函数用于使用request.session为当前用户的session data增加数据
def add_session_data(request):
    # 为当前用户的session data增加时间标识
    request.session['time']=ctime()

    return HttpResponse("增加session data")

# 查看当前用户session data的数据
def read_session(request):

    acquire = request.session.get("time")

    ret_Str = ""

    # 获取当前用户session data的数据
    for key , value in request.session.items():
        ret_Str+=f"{key}:{value}"

    return HttpResponse(f"当前用户的session data为{ret_Str}"
                        f"   By request.sesion.items()</br></br>"
                        f"{acquire}by request.session.get()")


# 删除当前用户session data的数据
def remove_session(request):
    # 删除session data内的某一键值对
    del request.session["time"]

    # 清空session data内的全部键值对，但数据库还有条目
    # request.session.clear()

    # 直接把当前用户对应的session内的数据库条目删除
    # request.session.flush()

    return HttpResponse("删除session data")
