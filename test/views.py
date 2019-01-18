from django.shortcuts import render,reverse
from django.http import  HttpResponse
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PatienceInfo
from .serialzer import  PatienceInfoSerialzer
# Create your views here.


# 反向解析
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
#
#
#
#
# # 插入商品
# no=PatienceInfo(
#     id = 1,
#     pname = '元十三箭',
#     pprice = 100,
#     psales=0,
#     pdescribe='好'
# )


#
# class PatInfo(APIView):
#
#
#     def get(self,request):
#
#         sps = PatienceInfo.objects.all()
#         print(sps,'----------------------------------')
#         sp = PatienceInfoSerialzer(sps)
#         return  Response(sp.data)
#
#
#
#
#     def post(self,request,pk):
#         try:
#             sps = PatienceInfo.objects.get(id=pk)
#         except PatienceInfo.DoesNotExist:
#             return  Response(status=status.HTTP_404_NOT_FOUND)
#
#         sp = PatienceInfoSerialzer(sps)
#         return  Response(sp.data)