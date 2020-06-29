from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


class BaseAccount(AbstractUser):
    email = models.EmailField(unique=True)
    check_staff = models.BooleanField(default=False)
    staff_id = models.CharField(max_length=15, blank=True, null=True, unique=True)

    def __str__(self):
        return self.username 


class UserProfile(models.Model):
    base = models.OneToOneField(BaseAccount, on_delete=models.CASCADE)

    dp = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Display picture")
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    delivery_address = models.CharField(max_length=1055, blank=True, null=True)
    contact_no = models.CharField(max_length=11, blank=True, null=True)

    user_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)




    def set_balance(self, value):
        self.balance = value
        

    def __str__(self):
        return self.base.username


        

"""
        Use these lines of code to set balance 

        profile.set_balance(20)
        profile.save();

"""


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=None, **kwargs):
    if created:
        Token.objects.create(user=instance)