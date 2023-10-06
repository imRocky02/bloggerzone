from django.contrib.auth.models import AbstractBaseUser, BaseUserManager 
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self,  email, password=None):
        """ 
        creates and save a user with the given email and password
        """
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_staffuser(self,  email, password=None):
        """ 
        creates and save a staff user with the given email and password
        """
        user = self.create_user(
            email,
            password=password,
            
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,   email, password=None):
        """ 
        creates and save a superuser with the given email and password
        """
        user = self.create_user(
            email,
            password=password, 
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user





class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    full_name = models.CharField(max_length=250)

    dob = models.DateField(verbose_name='Date OF Birth', default= timezone.now())
    
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [full_name, dob]


    
    # def full_name(self):
    #     return self.full_name
 
    
    # def dob(self):
    #     return self.dob

        # def get_full_name(self):
        #     return self.email

        # def get_short_name(self):
        #     return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # if obj and obj.is_active:
        #     return True          
        # else:
        #     return False
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    


    

    
