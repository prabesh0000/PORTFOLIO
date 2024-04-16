from django.db import models

# Create your models here.

from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    class meta:
        verbose_name_plural = 'skills'
        verbose_name_ = 'Skill'
  
    name =  models.CharField(max_length=20, blank=True, null= True)
    score = models.IntegerField (default=80,blank=True , null= True)
    image = models.FileField( blank= True, upload_to='Skills', max_length=100,null=True)
    is_key_skill =  models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    class meta:
            verbose_name_plural='User Profiles'
            verbose_name ='User Profile'

    user = models.OneToOneField (User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank= True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200 ,blank= True, null=True)
    bio = models.TextField(blank= True, null=True )
    skills = models.ManyToManyField(Skill, blank= True )
    cv = models.FileField(blank= True, null=True, upload_to="cv" )

    def __str__(self):
         return f'{self.user.first_name} {self.user.last_name}'
    


class ContactProfile(models.Model):
    class meta:
            verbose_name_plural='Contact Profiles'
            verbose_name ='Contact Profile'
            ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
  

    def __str__(self):
         return f'{self.name}'
         


class Testimonial(models.Model):
    class meta:
            verbose_name_plural='Testimonials'
            verbose_name ='Contact Profile'
            ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
  

    def __str__(self):
         return f'{self.name}'         