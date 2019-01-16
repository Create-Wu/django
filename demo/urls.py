"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import users.urls  # 导入子应用中的urls
# import users.views  #把路由写在总路由中,不设置子应用中的uslr.py,直接导入views(不推荐,不方便维护)
import response_json.urls
import  class_view.urls
import  test.urls,booktest_ORM.urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # include() 将users子应用下的所有路由都添加在主路由中
    # include() 除了可以传递字符串之外,还可以传递模块
    # url(r'^users/',include('users.urls'))

    url(r'^',include(users.urls)),
    # 也可以不设置子应用中的uslr.py,把所有路由都写在主路由中
    # url(r'^users/index/$',users.views.index)

    url(r'^',include(response_json.urls)),

    url(r'^',include(class_view.urls)),

    url(r'^', include(test.urls)),

    url(r'^',include(booktest_ORM.urls)),
]
