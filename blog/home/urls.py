from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from main_blog import views as main_blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^$', main_blog_views.blog, name='blog'),
]
