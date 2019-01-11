from django.conf.urls import url

from . import views



# urlpatterns 是Django 中自动识别的路由列表变量
urlpatterns = [
    # 每个路由都由url函数来构造
    # url(路径(正则匹配),视图)

    url(r'^index/$',views.index),
    # 正则表达式提取url中的参数,传递到视图函数是按顺序的
    url(r'^weather/([a-z]+)/(\d{4})/$',views.weather),

    #  正则表达式命名参数提取url中的参数,传递到视图函数是自行定义的名字
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$',views.weather),
    # 测试GET属性提取字符串
    url(r'^ps/',views.String),
    # 测试POST属性获取表单数据的请求体,django 默认开启csrf,由于未定义,所以此处需要在配置文件中把csrf注释
    url(r'^qs/',views.get_body),
    # 测试request.body属性获取json数据的请求体
    url(r'^json/',views.get_body_json),

    # 测试HttpResponse构建响应体
    url(r'^response/$',views.response_data),

    # 测试JsonResponse构建响应体
    url(r'^response_json/$',views.demo_view),

]