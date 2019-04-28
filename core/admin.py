from django.contrib import admin
from core.models import User, TrackerGroup, TrackerGroupInstance, Question, Answer, Response, TrackerGroupInstance

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'id',
        'name',
        'email',
        'slug',
    )

@admin.register(TrackerGroup)
class TrackerGroup(admin.ModelAdmin):
    list_display = (
        'name', 
        'user',
        'created_at', 
        'id',
    )

@admin.register(TrackerGroupInstance)
class TrackerGroupInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'tracker', 
        'started_at', 
        'created_by',
        'tracker_id',
    )

@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = (
        'current_question', 
        'tracker',
        'created_at', 
        'created_by',
    )

@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_display = (
        'current_answer', 
        'question',
        'created_at', 
        'created_by',
    )

@admin.register(Response)
class Response(admin.ModelAdmin):
    list_display = (
        'tracker', 
        'tracker_id',
        'tracker_instance_id',
        'question', 
        'question_id',
        'display_answers',
        'user',
        'created_at',
    )