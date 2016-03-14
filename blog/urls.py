"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include, patterns
from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', 'bloger.views.test'),
    url(r'^$','bloger.views.home', name='home'),
    url(r'^(?P<id>\d+)/$', 'bloger.views.detail', name='detail'),
    url(r'^archives/$', 'bloger.views.archives', name='archives'),
    url(r'^about_me/$', 'bloger.views.about_me', name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', 'bloger.views.search_tag', name='search_tag'),
    url(r'^search/$', 'bloger.views.blog_search', name='search'),
]
