from django.conf.urls import url

from . import views


urlpatterns = [


    #  注册类视图需要在视图名后面加as_view  手写as_view() 后面括号
    url(r'^class/$',views.Parent_View.as_view(),name='Anything')


]