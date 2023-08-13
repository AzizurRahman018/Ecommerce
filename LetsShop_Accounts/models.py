from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Address')
    company=models.CharField(max_length=100)
    town=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    phone_number=models.TextField()

    def __str__(self):
        return str(f'{self.user.username},{self.company}')