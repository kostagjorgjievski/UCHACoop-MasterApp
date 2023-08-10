from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models



class COOPUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, deposit_number, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not deposit_number:
            raise ValueError('The Deposit Number field must be set')
        if not password:
            raise ValueError('The Password field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, deposit_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not deposit_number:
            raise ValueError('The Deposit Number field must be set')
        if not password:
            raise ValueError('The Password field must be set')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, password, deposit_number, **extra_fields)


class COOPUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_current_member = models.BooleanField(default=True)
    deposit_number = models.CharField(max_length=5, unique=True)
    is_active = models.BooleanField(default=True)
    


    is_public_profile = models.BooleanField(default=False)


    # All coop roles
    is_itcrew = models.BooleanField(default=False)
    is_kitchencrew = models.BooleanField(default=False)
    is_facilitiescrew = models.BooleanField(default=False)
    is_board = models.BooleanField(default=False)
    is_memcom = models.BooleanField(default=False)
    is_storecrew = models.BooleanField(default=False)
    is_mailroomcrew = models.BooleanField(default=False)
    is_amocrew = models.BooleanField(default=False)
    is_socialcrew = models.BooleanField(default=False)
    is_gardencrew = models.BooleanField(default=False)
    is_admissions = models.BooleanField(default=False)
    is_roominspectioncrew = models.BooleanField(default=False)

    #superuser only Kosta Gjorgjievski
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'deposit_number']

    objects = COOPUserManager()  # We'll define this next

