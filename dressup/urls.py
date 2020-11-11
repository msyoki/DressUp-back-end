from .views import RegisterAPI,LoginAPI,ChangePasswordView,ProfilesAPI,ProfileAPI,ProductsAPI
from knox import views as knox_views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('api/profiles/', ProfilesAPI.as_view(), name='profiles'),
    path('api/profile/<int:pk>/',views.ProfileAPI),
    path('api/products/', ProductsAPI.as_view(), name='products'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)