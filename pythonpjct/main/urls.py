
from django.urls import path,include
from django.conf import settings
from .import views
from .views import *
from django.urls import re_path as url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.urls import path

## 

#urlpatterns = [
 #   path('',views.register,name='registration' ),
#]
urlpatterns = [
    path('', views.register, name='register'),
    path('/login', views.login, name='login'),
    
]
