from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View




def my_decorator(func):

    print('装饰器被调用')

    def wrapper(request,*args,**kwargs):
        print('被装饰了')
        return func(request,*args,**kwargs)
    return  wrapper


# 类视图，以及为类视图添加装饰器的使用
#method_decorator装饰器使用name参数指明被装饰的方法
class Parent_View(View):


    def get(self,request):

        return HttpResponse('test classview ')

    # 指定给post方法添加装饰器，在类视图中使用为函数视图准备的装饰器时，不能直接添加装饰器，
    # 需要使用method_decorator将其转换为适用于类视图方法的装饰器。
    @method_decorator(my_decorator)
    def post(self,request):

        return HttpResponse('test classview function')


# 类视图Mixin扩展类
#使用面向对象多继承的特性，可以通过定义父类（作为扩展类），在父类中定义想要向类视图补充的方法，
# 类视图继承这些扩展父类，便可实现代码复用。
#定义的扩展父类名称通常以Mixin结尾。

class listModelMixin(object):

    def list(self,*args,**kwargs):
        pass


class createModelMixin(object):

    def create(self,*args,**kwargs):

        pass

# 同时继承两个扩展类，复用list和create方法
class testModel(createModelMixin,listModelMixin,View):

    def get(self,request):
        self.list(request)


    def post(self,request):
        self.create(request)








