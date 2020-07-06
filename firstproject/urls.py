
from django.contrib import admin
from django.urls import path
import wordcount.views
import blog.views
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),
    path('blogs/', blog.views.blogs, name = "blogs"),
    path('my/', myapp.views.my, name = "my"),
]
