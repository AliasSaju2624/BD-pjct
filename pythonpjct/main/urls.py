
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
    path('listvideosbycategory', views.listvideosbycategory, name='listvideosbycategory'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('like-video/', views.like_video, name='like_video'),
    path('save_subscription/', views.save_subscription, name='save_subscription'),
    path('update_subscription/', views.update_subscription, name='update_subscription'),
    path('checkout/', views.checkout, name='checkout'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('users/', views.user_list, name='user_list'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('videos/', views.video_list, name='video_list'),
    path('videos/delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('make_payment', views.make_payment, name='make_payment'),
    path('create_admin_page/', views.create_admin_page, name='create_admin_page'),
    path('create_admin/', views.create_admin, name='create_admin'),
    path('update_user_info/', views.update_user_info, name='update_user_info'),
    path('update_info/', views.update_info, name='update_info'),
    path('generate_request/', views.generate_request, name='generate_request'),
    path('view_requests/', views.view_requests, name='view_requests'),
    
    



]
