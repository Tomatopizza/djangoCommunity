from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('User must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    username = models.CharField("사용자 이름", max_length=20, unique=True) 
    email = models.EmailField("이메일 주소", max_length=100, unique=True) # email 인증 때문에 erd에 없는데도 추가함.
    password = models.CharField("비밀번호", max_length=128)
    bio = models.TextField("자기소개", max_length=128, blank=True, default="")
    # imgfile = models.CharField("사진", max_length=128)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

