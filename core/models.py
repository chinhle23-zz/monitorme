from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse


class User(AbstractUser):
    """This model represents the customer user model"""
    
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    email = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    is_family_admin = models.BooleanField(default=False)
    label = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    active = models.BooleanField(default=True)
    phonenumber = models.CharField(max_length=25, null=True, blank=True)
    parent = models.ForeignKey('User', on_delete=models.CASCADE, default=1)
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
            return reverse('user_profile', kwargs={'slug': self.slug})

        def __str__(self):
            return self.username

class TrackerGroup(models.Model):
    """This model handles the group of questions a user creates for the tracker."""
    # Chinh added verbose name to name, available_to, and active fields
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='tracker name')
    available_to = models.ManyToManyField('User', verbose_name='assign users')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='set active')
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.id} {self.name}'

    def get_absolute_url(self):
        return reverse('tracker-detail', args=[str(self.id)])

class TrackerGroupInstance(models.Model):
    
    tracker = models.ForeignKey('TrackerGroup', related_name='tracker_instances', on_delete=models.CASCADE, null=False)
    start = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    end = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE,  null=False)

    def __str__(self):
        return f'{self.tracker.name} ({self.created_by.name})'


class Question(models.Model):
    """This creates the questionaire"""
    # Chinh added verbose name to description, order, tracker and active fields
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='question') 
    order = models.IntegerField(null=False, blank=False, verbose_name='order your question')
    tracker = models.ForeignKey('TrackerGroup', related_name='questions', on_delete=models.CASCADE, verbose_name='assign tracker')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='set active')
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.description   

    class Meta:
        ordering = ['tracker', 'order']

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])


class Answer(models.Model):
    """This creates the answer model"""
    # Chinh added verbose name to name, question, and active fields
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='answer')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='assign question')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='set active')
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('answer-detail', args=[str(self.id)])

class Response(models.Model):
    tracker = models.ForeignKey('TrackerGroup', 
    on_delete=models.CASCADE, null=False, blank=False)
    tracker_instance = models.ForeignKey('TrackerGroupInstance',  on_delete=models.CASCADE, null=False, blank=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False, blank=False)
    answer = models.ManyToManyField('Answer')
    answered_for = models.ForeignKey('User', on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'Response for: {self.tracker_instance.id} {self.tracker.name} ({self.answered_for.name})'

    def display_answers(self):
        """Create a string for the Answer(s). This is required to display answers in Admin."""
        return ', '.join(answer.name for answer in self.answer.all()[:3])







    
