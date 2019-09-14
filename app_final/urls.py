"""app_final URL Configuration

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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include
from best_cakes.views import BaseView, IndexView, AboutUsView, ElementsView, TortView, GenericView, GetInTouchView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^base/', BaseView.as_view(), name='base'),
    url(r'^index/', IndexView.as_view(), name='main'),
    url(r'^about_us', AboutUsView.as_view(), name='about_us'),
    url(r'^elements', ElementsView.as_view(), name='elements'),
    url(r'^tort', TortView.as_view(), name='tort'),
    url(r'^generic', GenericView.as_view(), name='tort'),
    url(r'^get_in_touch/', GetInTouchView.as_view(), name='get_in_touch')

]
