'''
This is userapi models module.
'''
import datetime
import uuid
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from storages.backends.s3boto3 import S3Boto3Storage

class MyUserManager(BaseUserManager):
    '''
    This is the manager class for MyUser model.
    '''
    def create_user(self, email, password, user_name, **extra_fields):
        """
        Create and save a User with the given email, fullname, and password.
        """
        if not email:
            raise ValueError('The user must have an email')

        if not password:
            raise ValueError('The user must have a password')

        if not user_name:
            raise ValueError('The user must have a user name')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, user_name, **extra_fields):
        """
        Create and save a SuperUser with the given email, fullname, and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, user_name, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    '''
    password field supplied by AbstractBaseUser
    last_login field supplied by AbstractBaseUser
    is_superuser field provided by PermissionsMixin if we use PermissionsMixin
    groups field provided by PermissionsMixin if we use PermissionsMixin
    user_permissions field provided by PermissionsMixin if we use PermissionsMixin
    '''
    USERNAME_FIELD = 'email'
    # while creating superuser from command it will ask these fields to enter value.
    REQUIRED_FIELDS = ['user_name', 'gender']
    # this is returned when we call get_email_field_name() method.
    EMAIL_FIELD = 'email'
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user_name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    gender = models.CharField(
        max_length=7,
        blank=False,
        null=False,
        choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    )
    img = models.ImageField(
        blank=True,
        null=True,
        storage=S3Boto3Storage(
            bucket_name='kisaa',
            region_name='us-east-1'
        ),
        upload_to='user/profile'
    )
    email_verified = models.BooleanField(verbose_name='Email Verified', default=False)
    is_active = models.BooleanField(
        default=True,
        help_text='Designates whether this user should be treated as active.\
            Unselect this instead of deleting accounts.',
    )
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.'
    )
    date_joined = models.DateTimeField(help_text='date joined', default=datetime.datetime.now())

    objects = MyUserManager()

    class Meta:
        '''
        This is the meta class for MyUser Model.
        '''
        ordering = ['-email',]

    def __str__(self):
        email = '%s' % (self.email)
        return email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perm_list, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_user_permissions(self):
        pass

    def get_group_permissions(self):
        pass

    def get_all_permissions(self):
        pass
