from django.urls import path
from . import views
from social_books import settings
# from .views import UserView
# from django.config import settings

from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('data/',views.show,name='author_seller'),
    path('upload/', views.create_profile,name="upload"),
    
    path('display_file',views.uploaded_file,name="display_file"),
    path('display_file_specific',views.uploaded_file_specific_user,name="display_file_specific"),
    # path('api/user/', UserView.as_view({'get': 'list'}), name='user_list'),
]


if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)