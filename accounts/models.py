from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
# from tickets.models import Ticket
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have email address")
        user    =   self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def search(self):
        return self.get_queryset().search(query=query)

        
    def create_superuser(self, email, password):
        user    =   self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email       =   models.EmailField(verbose_name="email", max_length=100, unique=True)
    name    =   models.CharField(max_length=30, blank=True)
    is_admin    =   models.BooleanField(default=False)
    is_active   =   models.BooleanField(default=True) 
    is_staff    =   models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)
    is_student =  models.BooleanField(default=True)
    date_joined =   models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login  =   models.DateTimeField(verbose_name="last login", auto_now=True)

    ''' setting the email as the required login field,
    but we can also user username if we so wish '''
    USERNAME_FIELD = 'email'

    objects =  UserManager()
    # @property
    # def num_post(self):
    #     num_post = Ticket.objects.filter(created_by__email=self.email).count()
    #     return num_post
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True