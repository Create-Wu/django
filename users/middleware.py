# 中间件 :

def simple_middleware(get_response):

    #此处编写的代码仅在Django 第一次配置和初始化的时候执行一次
    def middleware(request):
        #此处编写的代码会在每个请求处理视图前被调用。
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图函数之后被调用
        return  response

    return middleware




def my_middleware(get_response):
    print('init被调用')
    def middeware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after response 被调用')
        return response


    return  middeware





