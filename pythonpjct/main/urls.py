
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
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('upload-videos', views.upload_videos, name='upload_videos'),
    path('home', views.home, name='home'),
    path('popup', views.show_popup, name='popup'),
    path('myvideos', views.listmyvideos, name='listmyvideos'),
    path('listothervideos', views.listothervideos, name='listothervideos'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('like-video/', views.like_video, name='like_video'),
    path('save_subscription/', views.save_subscription, name='save_subscription'),
    path('checkout/', views.checkout, name='checkout'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('admin_home/', views.admin_home, name='admin_home'),
    



]
