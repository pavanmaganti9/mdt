"""blog URL Configuration

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
from django.urls import path
from home import views as home_views
from django.conf.urls import url
from main_blog import views as main_blog_views

admin.site.site_header = 'MDT Dashboard'                    # default: "Django Administration"
admin.site.index_title = 'Apps area'                 		# default: "Site administration"
admin.site.site_title = 'MDT' 								# default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^$', home_views.home, name='home'),
	url(r'^blog/$', main_blog_views.blog, name='blog'),
]
