from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,Product,Post


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        profile=Profile.objects.create(user=user,email=user.email,username=user)
        return user

# Change Password
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('username','first_name','last_name','email','phone','location','profile_pic')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('image','name','price','stock','size','category','username')
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('image','name','price','stock','size','category','username')



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','description','published')