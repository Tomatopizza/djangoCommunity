from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User


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
    
class Users(AbstractBaseUser):
    username = models.CharField("사용자 이름", max_length=20, unique=True) 
    email = models.EmailField("이메일 주소", max_length=100, unique=True) # email 인증 때문에 erd에 없는데도 추가함.
    password = models.CharField("비밀번호", max_length=128)
    bio = models.TextField("자기소개", max_length=128, blank=True, default="")
    # imgfile = models.CharField("사진", max_length=128)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
