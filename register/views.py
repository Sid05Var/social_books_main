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
# from djoser.views import UserViewSet


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        if email and password:
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
        else:
            return HttpResponse('Invalid email or password')
    
    return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'index.html', {'user_pr': user_pr})
    
    context = {"form": form}
    return render(request, 'profile_maker/create.html', context)



def uploaded_file(request):
    file=uploaded_files.objects.all()
    return render(request, 'display_uploaded_file.html',{'files':file})


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
    return render(request, 'display_uploaded_file.html',{'files':file})

    
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_uploaded_file(request, file_id):
    try:
        file = uploaded_files.objects.get(Title=file_id)
        # Perform any additional logic here if needed
        return Response({'file_url': file.display_picture.url})
    except uploaded_files.DoesNotExist:
        return Response({'error': 'File not found'}, status=404)