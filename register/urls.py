from django.urls import path
from . import views
from social_books import settings
from django.contrib.auth import views as auth_views
# from .views import UserView
# from django.config import settings

from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    # path('/logout/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('data/',views.show,name='author_seller'),
    path('upload/', views.create_profile,name="upload"),
    path('verify_otp/', views.verify_otp,name="verify"),
    
    path('display_file',views.uploaded_file,name="display_file"),
    path('display_file_specific',views.uploaded_file_specific_user,name="display_file_specific"),
    # path('api/user/', UserView.as_view({'get': 'list'}), name='user_list'),
    path('forget_password/', views.forget_password_send,name="forget_password_send"),
    path('reset_password/<str:reset_key>', views.confirm_password,name="reset_password"),
  
]


if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)