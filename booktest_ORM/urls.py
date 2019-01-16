from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views
from . import views_REST

urlpatterns = [

    url(r"^api/books/$",views_REST.BookListView.as_view()),
        #pk数字
    url(r"^books/(?P<pk>\d+)/$",views_REST.BooKDataView.as_view()),



]
#  把上面的注释掉，是因为可能其他路由把次路由覆盖了,也可以改上面的路由名
router=DefaultRouter()
# router.register(r'books',views.BookInfoViewSet)
# urlpatterns += router.urls