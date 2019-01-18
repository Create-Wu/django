from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework.views import APIView
from booktest_ORM.models import BookInfo
from booktest_ORM.serializer import BookInfoSerializer
from rest_framework.generics import GenericAPIView, ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import mixins
from rest_framework import viewsets, status
from rest_framework.viewsets import GenericViewSet,ReadOnlyModelViewSet
from rest_framework.decorators import action


#  视图集基类 APIView
# class BookListView(APIView):
#     def get(self, request):
#         # 查询所有书籍
#         books = BookInfo.objects.all()
#         serializers = BookInfoSerializer(books, many=True)  # 参数是查询集，many = True
#         return Response(serializers.data)  # .data  获取数据


#  视图集基类 GenericAPIView
# class BookDataView(GenericAPIView):
#     serializer_class = BookInfoSerializer  # 指定序列化器
#     queryset = BookInfo.objects.all()  # 指明数据查询集
#
#     #    #查询所有书籍
#     # def get(self, request):
#     #     books = self.get_queryset()  # 返回查询集
#     #     serializers = self.get_serializer(books, many=True)
#     #     return Response(serializers.data)
#
#     def get(self, request, pk):
#         books = self.get_object()
#         serializers = self.get_serializer(books)  # 参数不是查询集  不设many
#         return Response(serializers.data)


# GenericAPIView和Mixin扩展的结合
# class ListMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
# # 查询所有数据
# def get(self, request):
#     return self.list(request)
# #
# # # 新增数据
# def post(self, request):
#     return self.create(request)


#  使用继承GenericAPIVIew，ListModelMixin的子类视图
#  查询所有
# class BListView(ListAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


# -----------------------------------
#  视图集,查询所有和指定信息  ,定义路由时指定方法
#  url(r'^books/set/$',views.BookSetView.as_view({'get': 'list'})),
#  url(r'^books/set/(?P<pk>\d+)/$',views.BookSetView.as_view({'get': 'retrieve'})),
# class BookSetView(viewsets.ViewSet):
#
#     def list(self, rquest):
#         books = BookInfo.objects.all()
#         serialzers = BookInfoSerializer(books,many=True)
#         return Response(serialzers.data)
#
#     def retrieve(self, request, pk):
#
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#
#             return Response(status=status.HTTP_404_NOT_FOUND) # 返回错误代码
#         ps = BookInfoSerializer(book)
#         return Response(ps.data)


# GenericViewSet和继承Mixin扩展视图集
# GenericViewSet 提供了GenericAPIView的基础方法，所以不用再定义list方法
# url定义与上方一致
# class BookGenericView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer




# ReadonlyModelViewSet 视图父集  指定的方法行为
# class Book(mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
#
#
#     permission_classes = [IsAuthenticated]  # 仅通过认证的用户才有权限
#
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
#     # 指定可以过滤的字段
#     filter_fields = ['btitle','id']
#
#     #指定过滤后端为排序
#     filter_backends = [OrderingFilter]
#
#     # 指定可以排序的字段
#     ordering_filter = ['id','bread','bpud_date']
#
#     @action(methods=['get'],detail=False)
#     def latest(self,request):
#           # 返回最新id的书籍
#           book = BookInfo.objects.latest('id')
#           bs = BookInfoSerializer(book)
#           return  Response(bs.data)
#
#
#     @action(methods=['put'], detail=True)
#     def read(self,request,pk):
#          """修改阅读量"""
#          # url :as_view({'put':'read'})  修改数据使用put方式
#          books=self.get_object()
#          books.bread = request.data.get('bread')
#
#          books.save()
#          ps = BookInfoSerializer(books)
#          return  Response(ps.data)


# 作业
# class Test(RetrieveAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class =  BookInfoSerializer




# class Test(UpdateAPIView):
#         queryset = BookInfo.objects.all()
#         serializer_class =  BookInfoSerializer


class Test(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self,request,pk):

        try:
            sps= BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sp = BookInfoSerializer(sps)
        return Response(sp.data)



    def put(self,request,pk):

        try:
            sp= BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        sp.bread = request.data.get('bread',)  # 此处为小括号,元组中最后一个元素要逗号后
        sp.save()
        up=BookInfoSerializer(sp)
        return Response(up.data)

