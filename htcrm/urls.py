"""htcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from idlelib.multicall import r

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from APP import views
from APP.views import userlogin,userlist,adduser,delectuser,edituser,addtags,taglist,deltag,edittag,petlist,deletepet,addpet,editpet,test,CFVAdduser

urlpatterns = [
    path('admin/', admin.site.urls),
    url('login/',userlogin),
    url('userlist/',userlist),
    url('adduser/',views.CFVAdduser.as_view()), #CBV模式下调用类实现，里面的get,post方法名是固定写法，且需要导入整个文件，from APP import views
    # url('adduser/',adduser),  #FBV 模式下，调用法法实现
    url('delectuser/',delectuser),
    url('edituser/',edituser),
    url('addtags/',addtags),
    url('taglist/',taglist),
    url('deltag/',deltag),
    url('edittag/',edittag),
    url('petlist/',petlist),
    url('deletepet/',deletepet),
    url('addpet/',addpet),
    url('editpet/',editpet),
    url('test/',test)
]
