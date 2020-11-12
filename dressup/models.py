from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.contrib.auth.models import User

from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

# Profile Api
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profilepic/',default='default.jpeg')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    email = models.CharField(max_length=30,blank=True)
    phone = models.CharField(max_length=20)
    bio = models.CharField(max_length=500,blank=True)
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username

        


class Product(models.Model):
    image= models.ImageField(upload_to='productpic/',null=True)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    stock=models.IntegerField()
    size=models.CharField(max_length=30)
    category= models.ForeignKey('Category',on_delete = models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)



    def __str__(self):
        return self.name



CATEGOGY_CHOICES = (
    ("Men", "Men"),
    ("Ladies", "Ladies"),
    ("Kids", "Kids"),
)  
class Category(models.Model):
    name=models.CharField(max_length=30,choices=CATEGOGY_CHOICES)

    def __str__(self):
        return self.name


class Photo(models.Model):
  image = CloudinaryField('image')