from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404,reverse,HttpResponse
from django.core.files.storage import FileSystemStorage
from main.models import registration
from main.models import subscription
from main.models import Video
from django.contrib import messages
import boto3
import uuid
import stripe



# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        print(name)
        password=request.POST.get('password')
        print(password)
        password2=request.POST.get('password2')
        print(password2)
        email=request.POST.get('email')
        print(email)
        user=registration.objects.filter(name=name)
        if user:
            userdetails=registration.objects.get(name=name)
            messages.info(request, 'User already exist')
            return render(request,'registration.html')
        elif name =='':
            messages.info(request, 'Please provide name')
            return render(request,'registration.html')
        elif password =='':
            messages.info(request, 'Please password ')
            return render(request,'registration.html')
        elif password2 =='':
            messages.info(request, 'Please password ')
            return render(request,'registration.html')
        elif email =='':
            messages.info(request, 'Please password email ')
            return render(request,'registration.html')
        else:
            if (password==password2):
                registration(name=name,password=password,email=email).save()
                userinfo=registration.objects.get(name=name)
                print(userinfo.id)
                request.session['id']=userinfo.id
                request.session['username']=userinfo.name
                return render(request,'subscription.html')
            else:
            # context = "password not match"
                messages.info(request, 'Password does not match!')
                return render(request,'registration.html')
    else:
        return render(request,'registration.html')


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = registration.objects.filter(name=name, password=password).first()
        if user and user.active=='True' and user.admin=='False':
                request.session['id'] = user.id
                request.session['username'] = user.name
                user_subscription = subscription.objects.filter(username=name).first()
                request.session['subscription_type'] = user_subscription.category
                print(user.id)
                print(user.name)
                print(user_subscription.category)
                if user_subscription and user_subscription.category == 'premium':      
                    return render(request, 'home.html')
                else:
                    return render(request, 'basic_home.html')
        elif user and user.admin=='True':
                request.session['id'] = user.id
                request.session['username'] = name
                return render(request, 'admin_home.html') 
        else:
                messages.info(request, 'User not active or unauthorized')
    return render(request, 'login.html')

    
def change_details(request):
    changes = ["Added new feature X", "Fixed issue with login page", "Updated CSS styles"]
    return render(request, 'change_details.html', {'changes': changes})
def upload_videos(request):
    if request.method == 'POST' and request.FILES.get('video_file'):
        description = request.POST.get('description')
        category = request.POST.get('category')
        print(description)
        print(category)
        unique_value = str(uuid.uuid4())
        unique_value=unique_value+".mp4"
        print(unique_value)
        content_type = 'video/mp4'
        try:       
                
                    video_file = request.FILES['video_file']
                    video_key = description  # You might want to generate a unique key here
                    s3_client = boto3.client(
                        's3',
                        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    )
                    bucket_name = settings.AWS_STORAGE_BUCKET_NAME 
                    # Upload the video file to S3
                    s3_client.upload_fileobj(video_file, bucket_name, unique_value,ExtraArgs={'ContentType': content_type})
                    # Generate a presigned URL for the uploaded video
                    video_url = s3_client.generate_presigned_url(
                        'get_object',
                        Params={'Bucket': bucket_name, 'Key': unique_value},
                        ExpiresIn=3600  # Link expiration time in seconds
                        
                    )
                    
                    print(video_url)
                    id= request.session.get('id')
                    username= request.session.get('username')
                    print(id)
                    print(username)
                    Video(user_id=id,user_name=username,description=description,video_url=video_url,video_name=unique_value,category=category).save()
                    return HttpResponse(f'Video uploaded successfully! URL: {video_url}')
                
            
        except Exception as e:
                print(f"An error occurred: {e}")
                return HttpResponse('Error occurred while uploading the video.')
    
    return render(request, 'upload_video.html')
def listmyvideos(request):
    id = request.session.get('id')  # Assuming user ID is stored in session
    videos = Video.objects.filter(user_id=id)
    return render(request, 'my_videos.html', {'videos': videos})
def listothervideos(request):
    id = request.session.get('id')  # Assuming user ID is stored in session
    other_user_videos = Video.objects.exclude(user_id=id)
    return render(request, 'other_video.html', {'videos': other_user_videos})
def listvideosbycategory(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        videos_by_category =  Video.objects.filter(category=category).exclude(user_id=id)
    return render(request, 'other_video.html', {'videos': videos_by_category})
def like_video(request):
    if request.method == 'POST':
        video_id = request.POST.get('video_id')
        # Retrieve the video object based on the video ID
        video = Video.objects.get(id=video_id)
        # Increment the like count (assuming you have a 'likes' field in the Video model)
        video.likes += 1
        video.save()
        # Redirect back to the user's videos page or any other page
        return redirect('listothervideos')
    # Handle GET requests or other cases where the form is not submitted
    return redirect('listothervideos')
def save_subscription(request):
    if request.method == 'POST':
        subscription_type = request.POST.get('subscription_type')
        print(subscription_type)
        if(subscription_type=='premium'):
            return redirect('checkout')
        else:
            uid = request.session.get('id')
            uname=request.session.get('username')
            print("basic user id : ")
            print(uid)
            print(uname)
            subscription(category='basic',username=uname,userid=uid).save()
            return render(request,'basic_home.html')
    else:
        return render(request, 'subscription.html')

def home(request):
    subscription_type = request.session.get('subscription_type')
    if(subscription_type=='premium'):
        return render(request,'home.html')
    else:
        return render(request,'home.html')
def show_popup(request):
    return render(request, 'popup_message.html')
def user_logout(request):
    print('Logging out user')
    request.session.clear()
    print('Logging out user')
    return render(request,'login.html')
stripe.api_key = settings.STRIPE_SECRET_KEY
def checkout(request):
    return render(request, 'checkout.html')

def process_payment(request):
    if request.method == 'POST':
        token = request.POST.get('stripe_token')
        customer_name = request.POST.get('customer_name')  # Add customer name from form
        customer_address = request.POST.get('customer_address')  # Add customer address from form
        try:
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents (e.g., $10.00)
                currency='INR',
                source=token,
                description='Demo Charge',
                 shipping={
                    'name': customer_name,
                    'address': {
                        'line1': customer_address,
                        'city': 'Kottayam',  # Add city
                        'state': 'Kerala',  # Add state
                        'country': 'IN',  # Country code (IN for India)
                        'postal_code': '12345'  # Add postal code
                    }
                }
            )
            id = request.session.get('id')
            username= request.session.get('username') 
            subscription(category='premium',username=username,userid=id).save()
            return render(request, 'paymentsuccess.html')
        except stripe.error.CardError as e:
            # Payment failed, handle the error (e.g., display error message)
            return render(request, 'paymenterror.html', {'error_message': e.error.message})
    return render(request, 'checkout.html')


##############  Admin side #######################3
def admin_home(request):
    return render(request, 'admin_home.html')