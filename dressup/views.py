from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer,LoginUserSerializer, ChangePasswordSerializer,ProfileSerializer,ProductSerializer,PostSerializer
# from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated 
from .models import Profile,Product
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.db.models import Q

from rest_framework import viewsets, permissions, generics
# Create your views here.
# Register API

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })



# Login Api
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


#API to shows the user data when the user successfully logs in.
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


        
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

# Change password
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfilesAPI(APIView):
    def get(self, request, format=None):
        all_profiles =Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def ProfileAPI(request,pk):
    profile=Profile.objects.get(id=pk)
    serializers=ProfileSerializer(profile,many=False)
    return Response(serializers.data)

class ProductsAPI(APIView):
    def get(self, request, format=None):
        all_products =Product.objects.all()
        serializers = ProductSerializer(all_products, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def search_categoryAPI(request,search_term):
    products=Product.objects.filter(Q(category__icontains=search_term))
    serializers=ProductSerializer(products,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def search_productAPI(request,pk):
    product=Product.objects.get(id=pk)
    serializers=ProductSerializer(product,many=False)
    return Response(serializers.data)

class productpostAPI(generics.GenericAPIView):
    serializer_class=PostSerializer

    def post(self,request, format=None):
        current_user=request.user

        if request.method == 'POST':
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                # serializer.save(commit=False)
                user=request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
