from django.db import models

# Create your models here.
class registration(models.Model):
    name        =   models.CharField(max_length=100,unique=True)
    password    =   models.CharField(max_length=100)
    email        =   models.CharField(max_length=100,unique=True)
    active=models.CharField(max_length=50,default='True')
    admin=models.CharField(max_length=50,default='False')
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video_name=models.CharField(max_length=1000,default='null')
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    video_url=models.CharField(max_length=5000)
    likes = models.IntegerField(default=0)
    uploaded_date = models.DateTimeField(auto_now_add=True)
class subscription(models.Model):
    category        =   models.CharField(max_length=100)
    username    =   models.CharField(max_length=100)
    userid        =   models.CharField(max_length=100,unique=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)
class payments(models.Model):
    adminid=models.CharField(max_length=50,default='Demo')
    userid        =   models.CharField(max_length=100)
    videoid=models.CharField(max_length=50,default='Demo')
    amount=models.CharField(max_length=50,default='0')
    paymentdate       =   models.DateTimeField(auto_now_add=True)
class requests_generated(models.Model):
    userid        =   models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    comment=models.CharField(max_length=10000)
    requesteddate       =   models.DateTimeField(auto_now_add=True)
