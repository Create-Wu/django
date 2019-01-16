# from django.shortcuts import render,reverse
# from django.http import  HttpResponse
# from django.views import View
# # Create your views here.
#
#
# # 反向解析
# from test.models import PatienceInfo
#
#
# def Reqesp(request):
#     print(reverse('json_response'))
#
#     return HttpResponse('test reverse')
#
#
#
# #视图函数扩展类
# class ListModelMixin(object):
#
#     def list(self,request):
#         return  HttpResponse('XIXI')
#
#
#
# class CreateModelMixin(object):
#
#     def create(self,request):
#         return HttpResponse("HAHA")
#
#
# class BookView(ListModelMixin, CreateModelMixin,View):
#
#     def get(self,request):
#         self.list(request)
#         return HttpResponse('1',self.list(request))
#
#     def post(self,request):
#         self.create(request)
#         return HttpResponse('2')


from .models import PatienceInfo
from django.views import  View
from django.http import HttpResponse,JsonResponse
import json
# 插入商品
no=PatienceInfo(
    id = 1,
    pname = '元十三箭',
    pprice = 100,
    psales=0,
    pdescribe='好'
)




class PatienceListView(View):


    def get(self,request,pk):
        try:
            commodity= PatienceInfo.objects.get(id=pk)
        except  PatienceInfo.DoesNotExist:
            return HttpResponse({'message':'None pk'},status=404)

        commodity_dict={
            "id":commodity.id,
            "pname":commodity.pname,
            "pprice":commodity.pprice,
            "pcomment":commodity.pcomment,
            "psales":commodity.psales,
            "pdescribe":commodity.pdescribe
        }
        return JsonResponse(commodity_dict)

    def put(self,request,pk):
        json_str_dict = request.body
        json_str = json_str_dict.decode()
        json_data =json.loads(json_str)

        try:
            commodity =PatienceInfo.objects.get(id= pk)

        except PatienceInfo.DoesNotExist:
            return HttpResponse({'message':"None pk"},status=404)

        commodity.pprice = json_data['pprice']

        commodity_dict = {
            "id": commodity.id,
            "pname": commodity.pname,
            "pprice": commodity.pprice,
            "pcomment": commodity.pcomment,
            "psales": commodity.psales,
            "pdescribe": commodity.pdescribe
        }
        return JsonResponse(commodity_dict)