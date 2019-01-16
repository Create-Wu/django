from . import views,viewsORM
from django.conf.urls import url


urlpatterns=[

    url(r'^test/$',views.Reqesp),

    url(r'^BookView/$',views.BookView.as_view(),name='Class'),

    url(r'^Pat/(?P<pk>\d+)/$',viewsORM.PatienceListView.as_view())


]