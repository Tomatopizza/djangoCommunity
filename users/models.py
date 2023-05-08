from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='follwers') #서로 확인 누르지 않아도 팔로우 가능