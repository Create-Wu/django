from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse


# 测试Httpresponse构建响应对象
def response(request):
    Response = HttpResponse("You cannot find peace by avoiding life")
    Response['my_head'] = 'datou'  # 自定义响应头
    return Response


# 测试JsonResponse构建json响应对象

def json_response(request):
    # json_content = {"name":"wcx","level":"baofu"}
    json_content = [{"name": "wcx", "level": "baofu"}, {"name": "wcx", "level": "baofu"}]
    # 如果返回的不是字典需要把 safe设置为False
    return JsonResponse(json_content, safe=False)


# 反向解析 :  通过视图函数找到路径,（url中定义别名，根据别名找）
def reverse_dd(request):
    print(reverse('index'))

    return HttpResponse("test reverse ") #必须有返回对象


#  redirect 重定向
def redirect_demo(request):
    return redirect('/static/index.html')


# 测试cookie值设置
def cookie_demo(request):
    response = HttpResponse('cookie_demo')
    response.set_cookie("name", "dawu", max_age=60 * 60)
    return response


# 测试获取cookie值设置
# 通过COOKIE.get（“key”）
def demo_cookie(request):
    cookie_data = request.COOKIES.get('name')
    print(cookie_data)
    return HttpResponse('ok')


# 测试session设置及获取值
def get_session(request):


    # 通过request来设置和获取session，因为session依赖cookie，
    # 因为在设置session时会自动生成session_id随着response返回到cookie中，然后再请求对象中从cookie中
    # 提取到session_id再获取session值
    request.session['name'] = 'dawu'

    print(request.session['name'])

    return HttpResponse('get_session')
