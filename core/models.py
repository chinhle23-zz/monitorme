from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse


class User(AbstractUser):
    """This model represents the customer user model"""
    
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
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
    name = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey('User', related_name='trackers', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tracker-detail', args=[str(self.id)])
    


class TrackerGroupInstance(models.Model):
    tracker = models.ForeignKey('TrackerGroup', related_name='tracker_instances', on_delete=models.CASCADE, null=False)
    started_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE,  null=False)

    def __str__(self):
        return self.tracker.name

    class Meta:
        ordering = ['started_at']


class Question(models.Model):
    """This creates the questionaire"""
    current_question = models.TextField(max_length=1000, null=False, blank=False) 
    tracker = models.ForeignKey('TrackerGroup', related_name='questions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.current_question  

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])


class Answer(models.Model):
    """This creates the answer model"""
    current_answer = models.CharField(max_length=100, null=False, blank=False)
    question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['current_answer']

    def get_absolute_url(self):
        return reverse('answer-detail', args=[str(self.id)])

    def __str__(self):
        return self.current_answer

class Response(models.Model):
    tracker = models.ForeignKey('TrackerGroup', 
    on_delete=models.CASCADE, null=False, blank=False)
    tracker_instance = models.ForeignKey('TrackerGroupInstance',  on_delete=models.CASCADE, null=False, blank=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False, blank=False)
    answers = models.ManyToManyField('Answer', related_name="response_answers")
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.tracker.name} {self.created_at} {self.answers}'

    def display_answers(self):
        """Create a string for the Answer(s). This is required to display answers in Admin."""
        return ', '.join(answer.current_answer for answer in self.answers.all()[:3])







    
