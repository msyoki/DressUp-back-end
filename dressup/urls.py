from .views import RegisterAPI,LoginAPI,ChangePasswordView,ProfilesAPI,ProfileAPI,ProductsAPI,search_categoryAPI,search_productAPI,productpostAPI
from knox import views as knox_views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('profiles/', ProfilesAPI.as_view(), name='profiles'),
    path('profile/<int:pk>/',views.ProfileAPI ,name='profile'),
    path('products/', ProductsAPI.as_view(), name='products'),
    path('product/<int:pk>/',views.search_productAPI ,name='profile'),
    path('newproduct/', productpostAPI.as_view(), name='newproduct'),
    path('search/<str:search_term>/',views.search_categoryAPI ,name='search_category'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)