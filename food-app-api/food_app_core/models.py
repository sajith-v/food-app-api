from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self,FirstName,LastName,Email, password, **otherFields):
        if not Email:
            raise ValueError('email is required')
        if not FirstName:
            raise ValueError('first name is required')
        if not LastName:
            raise ValueError('last name is required')

        user = User(FirstName=FirstName, LastName=LastName, Email= self.normalize_email(Email),**otherFields)
        user.set_password(password)
        user.save(using=self._db)
        return user;

    def create_superuser(self,Email, password, firstname = None, lastname = None, **otherFields):
        if not firstname:
            firstname = Email
        if not lastname:
            lastname = Email
        user = self.create_user(firstname,lastname,Email,password)
        user.is_superuser = True
        user.save(using=self._db)
        return user;




class User(AbstractBaseUser, PermissionsMixin):
    Email = models.EmailField(max_length=255, unique=True,null=False,blank=False)
    FirstName = models.CharField(max_length=255,null=False,blank=False)
    LastName = models.CharField(max_length=255,null=False,blank=False)
    IsActive = models.BooleanField(null=False,blank=False,default=False)

    objects = UserManager()
    USERNAME_FIELD = 'Email'

    @property
    def is_active(self):
        "Is the user active?"
        return self.IsActive

    @property
    def email(self):
        return self.Email




