"""
URL configuration for social_books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
# from users.views import show
from register.views import show
from register.views import TokenGenerationView
from register.views import get_uploaded_file
# from djoser.views import TokenCreateView, TokenDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('register.urls')),
    path('upload/', include('upload_book_app.urls')),
    path('info/', show),
    path('api/token/', TokenGenerationView.as_view(), name='token_generation'),
    path('files/<str:file_id>/', get_uploaded_file, name='get_uploaded_file'),
    # path('api/', include('djoser.urls')),
    # path('api/', include('djoser.urls.jwt')),
    # path('api/token/create/', TokenCreateView.as_view(), name='token_create'),
    # path('api/token/destroy/', TokenDestroyView.as_view(), name='token_destroy'),

]

