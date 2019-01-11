from django.conf.urls import url
from . import views

urlpatterns = [

    url(r"^rend/$", views.response, name='index'),

    url(r"^rend_json/$", views.json_response, name="json_response"),

    url(r'^redirect_demo/$', views.redirect_demo),

    url(r'^reverse_dd/$', views.reverse_dd),

    url(r'^cookie_demo/$', views.cookie_demo),

    url(r'^demo_cookie/$', views.demo_cookie),

    url(r'^demo_session/$', views.get_session),

]
