from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views
from . import views_REST
from rest_framework import  routers

urlpatterns = [
    #
    # url(r"^books/$", views.BookListView.as_view()),
    # #     #pk数字
    # url(r"^api/books/(?P<pk>\d+)/$", views.BookDataView.as_view()),
    #
    # # GenericAPIView和Mixin扩展的结合
    # url(r'^books/list/$', views.ListMixinView.as_view()),

    #使用继承GenericAPIVIew，ListModelMixin的子类视图ListAPIView
    # url(r'^books/Blist/$', views.BListView.as_view()),

    #  视图集
    # url(r'^books/set/$',views.BookSetView.as_view({'get': 'list'})),
    # url(r'^books/set/(?P<pk>\d+)/$',views.BookSetView.as_view({'get': 'retrieve'})),


    # GenericViewSet视图集
    # url(r'^books/geneset/$',views.BookGenericView.as_view({'get':'list'})),
    # url(r'^books/set/(?P<pk>\d+)/$',views.BookGenericView.as_view({'get': 'retrieve'})),

    # GenericViewSet指定的自定义方法
    #   url(r'^book/$',views.Book.as_view({'get':'list'})),
    #   url(r'^book/read/(?P<pk>\d+)/$',views.Book.as_view({'put':'read'}))
    # 每日作业
        url(r'^sp/(?P<pk>\d+)$',views.Test.as_view()),
        # url(r'^sp/$',views.Test.as_view()),

]

# ViewSet视图集路由
# router = routers.SimpleRouter()
# router.register(r'^books',views.Book,base_name='book')
# urlpatterns += router.urls



#  把上面的注释掉，是因为可能其他路由把次路由覆盖了,也可以改上面的路由名
# router=DefaultRouter()
# router.register(r'books',views.BookInfoViewSet)
# urlpatterns += router.urls