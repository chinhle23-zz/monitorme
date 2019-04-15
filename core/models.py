from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse


class User(AbstractUser):
    """This model represents teh customer user model"""
    
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    email = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    is_family_admin = models.BooleanField(default=False)
    label = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    phonenumber = models.CharField(max_length=25, null=True, blank=True)
    slug = models.SlugField()

    def set_slug(self):
        """Creates a unique slug"""
        if self.slug:
            return

        def save(self, *args, **kwargs):
            """creates unique slug"""
            self.set_slug()
            super().save(*args, **kwargs)

        def get_absolute_url(self): 
            return reverse('user-profile', kwargs={'slug': self.slug})

        def __str__(self):
            return self.username

# class Group(models.Model):
#     """This creates a group to assign """
#     name = models.CharField(max_length=100, null=False, blank=False)
#     users = models.ForeignKey('User', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

class TrackerGroup(models.Model):
    """This model handels the group of questions a user creates for the tracker."""
    name = models.CharField(max_length=100, null=False, blank=False)
    available_to = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    """This creates the questionaire"""
    description = models.TextField(max_length=1000, null=False, blank=False) 
    order = models.CharField(max_length=1000, null=False, blank=False)
    tracker = models.ForeignKey('TrackerGroup', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)


class Answer(models.Model):
    """This creates the answer model"""
    name = models.CharField(max_length=100, null=False, blank=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Response(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    answered_for = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)








    
