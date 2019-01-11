from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

import json
# 测试定义路由
def index(request):
    """

    :param request:包含了请求信息的请求对象
    :return:
    """
    return HttpResponse("Anything in life worth having would take seatrifice patience,and be a lot of work")

# 测试正则表达式获取url请求参数
#  url(r'(?P<city>[a-z]+)/(?P<year>\d{4})/$',urls.weather)
#  127.0.0.1:8000/weather/beijing/2018
def weather(request,city,year):

    print(city)
    print(year)

    return HttpResponse('OK')


# 运用django中的GET属性获取url请求中的字符串参数
# /qs/?a=1&b=2&a=3
def String(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    a_list = request.GET.getlist('a')

    print(a)  # 3
    print(b)  # 2
    print(a_list) #['1','3']

    return HttpResponse('OK')


# 运用django中的POST属性获取前端发送表单类型请求体的数据
# 用postman测试,post请求方式,要把csrf注释

def get_body(request):

    a = request.POST.get('a')
    b = request.POST.get('b')
    a_list = request.POST.getlist('a')

    print(a)
    print(b)
    print(a_list)

    return HttpResponse('OK')

# 非表单类型(json)的请求体数据，Django无法自动解析，可以通过request.body属性获取最原始的请求体数据
# 用postman测试,post请求方式,要把csrf注释
# JSON : {'a': 1,'b' :2}

def get_body_json(request):

    json_data = request.body
    json_data_deco = json_data.decode()
    body_str = json.loads(json_data_deco)
    print(body_str)

    return HttpResponse('OK')



def response_data(request):

    # return HttpResponse('Aaything in life', status=400)

    reponse = HttpResponse('itcast','python')

    reponse.status_code = 400
    reponse['Itcast'] = 'python'
    return  reponse


def demo_view(request):


    return JsonResponse({"we this having sb":"you","age":18})






