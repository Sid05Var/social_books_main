import string
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import Profile_form
from .models import uploaded_files
from .wrapper import my_books_wrapper
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from social_books import settings
from django.contrib.auth.hashers import make_password
# from .models import ver_otp
# from .forms import V_otpform
from django.core.mail import send_mail
import math, random

# from djoser.views import UserViewSet 


def login(request):   
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        otp=generateOTP()
        request.session["otp"] = otp
        request.session["email"]=email
        request.session["password"]=password
        if email and password:
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                from_email = settings.EMAIL_HOST_USER
                send_mail("otp", otp, from_email, [email])
                print("otp", otp, from_email, [email])
                return redirect('verify')
        else:
            return HttpResponse('Invalid email or password')
    
    return render(request, 'login.html')

def verify_otp(request):
    otp = request.session.get("otp")
    email=request.session.get("email")
    password=request.session.get("password")
    # form1=V_otpform()
    if request.method == 'POST':
        ent_otp = request.POST.get("enterotp")
        print(ent_otp)
        if str(ent_otp) == str(otp):
            user = authenticate(username = email, password = password)
            auth_login(request,user)
            return redirect('index')
        
        else:
            return HttpResponse('otp is invalid')
    return render(request, 'verify.html')
            
def forget_password_send(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        global global_email, global_key
        global_email = email
        reset_key = generate_activation_key()
        global_key = reset_key
        link = f"http://localhost:8000/reset_password/{reset_key}"
        from_email = settings.EMAIL_HOST_USER
        send_mail("Forget link", link, from_email, [email])
        print("Forget link", link, from_email, [email])
        return redirect("login")
    return render(request,"forgot-password.html")

def confirm_password(request,reset_key):
    global global_email, global_key
    print(global_email,global_key)
    if request.method == 'POST':
        p1=request.POST.get('passwordone')
        p2=request.POST.get('passwordtwo')
        if str(p1) == str(p2):
            user = CustomUser.objects.get(email=global_email)
            print(user)
            user.password=make_password(p1)
            user.save()
            return redirect('login')
    return render(request,"otp_reset.html")
    

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        
        if form.is_valid():
            form.save()
            subject = 'Social Book Registration'
            message = f'Hello {fullname}, You have been registered with us successfully. Please verify your email by clicking on this link: '
            from_email = settings.EMAIL_HOST_USER
            to_email = email
            print(to_email)
            send_mail(subject, message, from_email, [to_email])
            print(subject, message, from_email, [to_email])
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
@login_required(login_url='login')
def show(request):
    user_first_name = request.user.email
    info = CustomUser.objects.all()#.filter(email="sidvarangaonkar5@gmail.com")
    return render(request, 'info.html', {'info': info})



IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_profile(request):
    form = Profile_form()
    if request.method == 'POST':
        form = Profile_form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     return render(request, 'profile_maker/create.html')
            user_pr.save()
            return render(request, 'index.html', {'user_pr': user_pr})
    
    context = {"form": form}
    return render(request, 'profile_maker/create.html', context)



def uploaded_file(request):
    file=uploaded_files.objects.all()
    return render(request, 'product.html',{'files':file})


# class UserView(UserViewSet):
#     queryset = CustomUser.objects.all()

@my_books_wrapper
def uploaded_file_specific_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
        file=uploaded_files.objects.all()
        if username is not None:
            file=file.filter(Name = username)
    return render(request, 'product.html',{'files':file})

    
class TokenGenerationView(APIView):
    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
        
        
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_uploaded_file(request, file_id):
#     try:
#         username=request.user.username
#         # file = uploaded_files.objects.get(Title=file_id)
#         file=uploaded_files.objects.all()
#         file=file.filter(Name=username)
#         # Perform any additional logic here if needed
#         return Response({'file_url': file.display_picture.url,'file_Title':file.Name,'file_Cost':file.Cost,'file_year_of_publish':file.year_of_pblish,'file_visibility':file.visibility})
#     except uploaded_files.DoesNotExist:
#         return Response({'error': 'File not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_uploaded_file(request):
    try:
        username=request.user.username
        dict={}
        dict1={}
        # file = uploaded_files.objects.get(Title=file_id)
        file=uploaded_files.objects.all()
        print(username)
        file=file.filter(Name=username)
        print(file)
        for i in file:
            b=i.display_picture.url
            b=b.split("/")
            print(b)
            c=""
            c=b[2]
            dict1[i.Title]={'file_url': c,'file_Title':i.Title,'file_Cost':i.cost,'file_year_of_publish':i.year_of_pblish,'file_visibility':i.visibility}
            print(dict1)
            
            a={'file_url': i.display_picture,'file_Title':i.Name,'file_Cost':i.cost,'file_year_of_publish':i.year_of_pblish,'file_visibility':i.visibility}
        # Perform any additional logic here if needed
        # dict1=tuple(dict1)
        print(dict1)
        return Response({'file_details':dict1})
    except uploaded_files.DoesNotExist:
        return Response({'error': 'File not found'}, status=404)

    # .display_picture.url,'file_Title':file.Name,'file_Cost':file.Cost,'file_year_of_publish':file.year_of_pblish,'file_visibility':file.visibility
# 'Name',
#             'Title',
#             'visibility',
#             'cost',
#             'year_of_pblish',
#             'display_picture',
    
def generateOTP() :
     
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

def generate_activation_key():
    chars = string.ascii_letters + string.digits
    activation_key = ''.join(random.choice(chars) for _ in range(16))
    return activation_key


