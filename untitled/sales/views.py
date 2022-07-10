# 装载redirect和render
from django.shortcuts import render,redirect

# 装载HttpResponse
from django.http import HttpResponse

# 将公用数据库common装载进来
from common.models import Customer

# 导入json库
import json

# 导入django对template的加载工具
from django.template.loader import get_template

# 导入类视图的父类View
from django.views import View




# 该函数用来验证   重定向的使用。
def list_orders(request):
    return redirect("/sales/customers/")        # 重定向到下面那个查询Customer元素的路由

# 查询customer内的所有元素
def list_customers(request):
    query_set = Customer.objects.values()

    print(type(query_set))

    ret_Str=""

    for i in query_set:
        for key,value in i.items():
            ret_Str+=f"{key}:{value}</br>"
        ret_Str+="</br>"

    return HttpResponse(ret_Str)


# 过滤查询customer内的元素
def select_list_customers_byPhoneNumber(request):
    query_set = Customer.objects.values()

    vue = request.GET.get("phoneNumber",None)      # 尝试性接收phoneNum，存在则赋值给vue，不存在vue=None
    print(vue)
    if vue:
        query_set= query_set.filter(phoneNumber=vue)
        if not query_set:
            return HttpResponse(f"没有手机号为{vue}的查询结果")
        else:
            ret_Str = ""

            for i in query_set:
                for key, value in i.items():
                    ret_Str += f"{key}:{value}</br>"
                ret_Str += "</br>"

            return HttpResponse(ret_Str)
    else:
        return HttpResponse("查询条件不符合")

# 该函数用于ORM操作db的测试
def db_test(request):
    # 修改表中一行数据error
    # tmp = Customer.objects.get(id=6)    # 返回的是具体对象，没有update方法
    Customer.objects.filter(id=6).update(email="0010@qq.com")

    # 修改表中多行数据（也就是先filter再update   略）

    return HttpResponse("修改")

# 该函数用于从url中获取url参数
def get_info_from_url(request,id):

    ret_Str = "What information can you get from URL?</br>"

    ret_Str += f"id:{id}"

    return HttpResponse(ret_Str)

# 该函数用于从get请求中，获取get参数
def obtain_from_GET(request):
    ret_Str = "What information can you obtain from GET?</br>"

    question_id = request.GET.get("q_id")
    user_id = request.GET.get("u_id")

    get_list = request.GET.getlist('u_id')
    print(get_list)

    ret_Str += f"question_id:{question_id}  </br>"
    ret_Str += f"user_id:{user_id}"

    return HttpResponse(ret_Str)

# 该函数用于从post请求中，获取参数
def obtain_from_POST(request):

    name = request.POST.get("name")

    return HttpResponse(name)

# 该函数用于从json中，获取参数
def obtain_from_json(request):
    # 获取json数据
    json_bytes = request.body

    # 转换json数据类型为字典类型
    json_Str = json_bytes.decode()

    # 转换为字典
    json_dict = json.loads(json_Str,encoding = 'utf-8')

    # 展示数据
    ret_Str = ""
    for key,value in json_dict.items():
        ret_Str += f"{key}:{value}</br>"

    return HttpResponse(ret_Str)


# 该函数调用html模板
def show_template_index(request):
    # 查询所有销售人员的信息，赋给context字典
    query_set = Customer.objects.values()

    # 获取template目录下的模板赋给template1
    template1 = get_template('sales_index.html')

    # 构造context字典作为参数
    context = {
        "data":query_set,
        'ret_state':0
    }

    # 渲染模板（并传参）
    res = template1.render(request=request, context=context)

    # 返回响应给浏览器
    return HttpResponse(res)

# 该函数为了体现  模板的继承与重写 而写
def show_excellent_staff(request):

    template=get_template('excellent_staffs.html')

    res = template.render(request=request)

    return HttpResponse(res)

# 该类为 类视图
class Curd(View):               # 继承自Django的View
    query_set = Customer.objects.values()

    def get(self , request):        # 重写get请求的处理查
        ret_Str = ""

        for i in self.query_set:
            for key, value in i.items():
                ret_Str += f"{key}:{value}</br>"
            ret_Str += "</br>"

        return HttpResponse(ret_Str)

    def post(self , request):       # 重写post请求的处理增
        name = request.POST.get('name')

        phoneNumber = request.POST.get('phoneNumber')

        address = request.POST.get('address')

        email = request.POST.get('email')

        Customer.objects.create(name=name,phoneNumber=phoneNumber,address=address,email=email)

        return HttpResponse("增  OK")
