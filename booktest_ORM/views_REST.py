# from django.http import HttpResponse, JsonResponse
# from booktest_ORM.models import BookInfo, HeroInfo
# from django.views import View
# import json

"""
GET    /books/  提供所有记录
POST   /books/   新增一条记录
PUT    /books/<pk>/  修改指定的id记录
GTE    /books/<pk>/   提供指定的id记录
DELETE  /books/<pk>/   删除指定id记录
响应数据  json

"""
#
#
# class BookListView(View):
#     # 提供所有记录
#     def get(self, request):
#         books = BookInfo.objects.all()
#
#         books_list = []
#
#         for book in books:
#             book_dict = {
#                 "id": book.id,
#                 "btitle": book.btitle,
#                 "bpud_date": book.bpud_date,
#                 "bcomment": book.bcomment,
#                 "bread": book.bread,
#                 # "image": book.image.url if book.image else "",
#             }
#             books_list.append(book_dict)
#             # 返回的不是字典,要把safe 设为false
#         return JsonResponse(books_list, safe=False)
#
#     # 新增一条记录
#     def post(self, request):
#         json_str_bytes = request.body
#         json_str = json_str_bytes.decode()
#         json_data = json.loads(json_str)
#
#         book = BookInfo.objects.create(
#             btitle=json_data.get('btitle'),
#             bpud_date=json_data.get('bpud_date'),
#         )
#         book_dict = {
#             "id": book.id,
#             "btitle": book.btitle,
#             "bcomment": book.bcomment,
#             "bread": book.bread,
#             "bpud_date": book.bpud_date,
#             # "image":book.image.url if book.image else ''
#         }
#         # 新增状态吗 201
#         return JsonResponse(book_dict, status=201)
#
#
# class BookDataView(View):
#     # 提供指定的id记录
#     def get(self, request, pk):
#         # 1.查询
#         try:
#
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse({'errno': 'pk不存在'}, status=404)
#
#         book_dict = {
#             "id": book.id,
#             "btitle": book.btitle,
#             "bcomment": book.bcomment,
#             "bread": book.bread,
#             "bpud_date": book.bpud_date,
#             # "image":book.image.url if book.image else ""
#
#         }
#         return JsonResponse(book_dict)
#
#     # 修改指定的id记录
#     def put(self, request, pk):
#
#         json_str_bytes = request.body
#         json_str = json_str_bytes.decode()
#         json_dict = json.loads(json_str)
#
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse({"errno": 'pk不存在'}, status=404)
#
#         book.btitle = json_dict['btitle']
#         book.bpud_date = json_dict['bpud_date']
#         book.bread = json_dict.get('bread', book.bread)
#         book.save()
#
#         book_dict = {
#             "id": book.id,
#             "btitle": book.btitle,
#             "bcomment": book.bcomment,
#             "bread": book.bread,
#             "bpud_date": book.bpud_date,
#         }
#         return JsonResponse(book_dict)
#
#     # 删除指定的id记录
#     def delete(self, request, pk):
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse({"errno": 'pk不存在'}, status=404)
#         book.delete()
#
#         return HttpResponse('')


from django.views import View
from booktest_ORM.models import BookInfo
from django.http import JsonResponse, HttpResponse
import json

"""
GET    /books/  提供所有记录
POST   /books/   新增一条记录
PUT    /books/<pk>/  修改指定的id记录
GTE    /books/<pk>/   提供指定的id记录
DELETE  /books/<pk>/   删除指定id记录
响应数据  json

"""


class BookListView(View):
    #  提供所有记录
    def get(self, request):
        # 1).获取参数,得到查询集
        books = BookInfo.objects.all()

        # 全部数据装在列表里
        book_list = []

        for book in books:
            book_dict = {
                "id": book.id,
                "btitle": book.btitle,
                "bread": book.bread,
                "bcomment": book.bcomment,
                "bpud_date": book.bpud_date,

            }
            book_list.append(book_dict)
            #  JsonResponse返回的列表，所以safe改false
        return JsonResponse(book_list, safe=False)

    # 新增记录
    def post(self, request):
        # 获取json数据
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        json_dict = json.loads(json_str)

        # 创建数据
        book = BookInfo.objects.create(
            btitle=json_dict.get("btitle"),
            bread=json_dict.get("bread"),
            bpud_date=json_dict.get("bpud_date"),

        )
        # 转换成字典
        book_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bcomment": book.bcomment,
        }

        return JsonResponse(book_dict, status=201)


class BooKDataView(View):
    # 获取指定id记录
    def get(self, request, pk):
        try:
            # 查询id对应数据
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'massage': "pk不存在"}, status=404)

        book_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bread": book.bread,
            "bcomment": book.bcomment,
            "bpud_date": book.bpud_date,
        }

        return JsonResponse(book_dict)

    # 修改指定记录数据
    def put(self, request, pk):
        # 获取json数据
        json_str_dict = request.body
        json_str = json_str_dict.decode()
        json_dict = json.loads(json_str)

        # 替换数据
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({"massage": "pk不存在"}, status=404)

        book.btitle = json_dict['btitle']
        book.bpud_date = json_dict['bpud_date']
        book.bcomment = json_dict['bcomment']

        book_dict = {

            "btitle": book.btitle,
            "bcomment": book.bcomment,
            "bpud_date": book.bpud_date,

        }
        return JsonResponse(book_dict)

    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({"massage": "pk不存在"}, status=404)

        book.delete()

        return HttpResponse("")
