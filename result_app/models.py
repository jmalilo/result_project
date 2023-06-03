from django.db import models
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin
from django.core.validators import MinValueValidator,MaxValueValidator
from django.conf import settings
from datetime import timedelta,date

# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('You have not provided valid email')
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email,password,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,blank=False,null=False)
    password=models.CharField(max_length=200)
    full_name=models.CharField(unique=True,max_length=90,blank=True,null=True)
    phone_1=models.CharField(max_length=50)
    phone_2=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True,blank=True,null=True)
    is_staff=models.BooleanField(default=False,blank=True,null=True)
    is_superuser=models.BooleanField(default=False,blank=True,null=True)

    USERNAME_FIELD='email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
    def get_short_name(self):
        return self.full_name or self.email.split('@')[0]
    
class Student(models.Model):
    parent=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    full_name=models.CharField(max_length=100)
    class_level=models.ForeignKey('LevelClass',on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name
class Fee(models.Model):
    parent=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    stud_name=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='fees')
    required_amount=models.IntegerField()
    amount_paid=models.IntegerField()
    month_paid=models.CharField(max_length=300,choices=(('JANUARY','JANUARY'),('FEBRUARY','FEBRUARY'),('MARCH','MARCH'),('APRIL','APRIL'),('MAY','MAY'),('JUNE','JUNE'),('JULY','JULY'),('AUGUST','AUGUST'),('SEPTEMBER','SEPTEMBER'),('OCTOBER','OCTOBER'),('NOVEMBER','NOVEMBER'),('DECEMBER','DECEMBER')),blank=True,null=True )
    debt=models.IntegerField()
    date_paid=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.stud_name.full_name
    
class LevelClass(models.Model):
    name=models.CharField(max_length=200)
    class Meta:
        verbose_name_plural='LevelClasses'

    def __str__(self):
        return self.name

class Result(models.Model):
    email=models.EmailField(blank=True,null=True)
    stud_name=models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='Student Name',related_name='results')
    date_posted=models.DateField(auto_now_add=True)
    date_edited=models.DateField(auto_now_add=True)
    #subjects
    # arithmetic
    arithmetic=models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    arithmetic_grade=models.CharField(max_length=2,blank=True,null=True)
    arithmetic_grade_comment=models.CharField(max_length=100,blank=True,null=True)

    # english_language
    e_language=models.IntegerField(blank=True,null=True,verbose_name='English Language',validators=[MinValueValidator(0),MaxValueValidator(100)])
    e_language_grade=models.CharField(max_length=2,blank=True,null=True)
    e_language_grade_comment=models.CharField(max_length=100,blank=True,null=True)

    # kiswahili
    kiswahili=models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    kiswahili_grade=models.CharField(max_length=2,blank=True,null=True)
    kiswahili_grade_comment=models.CharField(max_length=100,blank=True,null=True)

    # pre_science
    pre_science=models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    pre_science_grade=models.CharField(max_length=2,blank=True,null=True)
    pre_science_grade_comment=models.CharField(max_length=100,blank=True,null=True)

    # writing
    writing=models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    writing_grade=models.CharField(max_length=2,blank=True,null=True)
    writing_grade_comment=models.CharField(max_length=100,blank=True,null=True)

    total=models.IntegerField(blank=False,null=False)
    average=models.IntegerField(blank=False,null=False)
    grade=models.CharField(max_length=3,blank=False,null=False,default='')
    pos=models.CharField(max_length=3,blank=True,null=True,default='')
    
    class Meta:
        ordering=['-date_posted']


    def __str__(self):
        return 'Results for '+self.stud_name.full_name
   

    def is_new(self)->bool:
        if date.today() < self.date_posted+timedelta(days=7):
            return True
        return False


