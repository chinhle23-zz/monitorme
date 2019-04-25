from django.contrib import admin
from core.models import User, TrackerGroup, Question, Answer, Response, TrackerGroupInstance

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'name',
        'email',
        'is_family_admin',
        'label',
        'created_at',
        'updated_at',
        'city',
        'state',
        'zipcode',
        'active',
        'phonenumber',
        'password',
    )
    exclude= ('slug',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'description', 
        'order', 
        'tracker', 
        'active',
        'id',
    )

@admin.register(TrackerGroupInstance)
class TrackerGroupInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'tracker', 
        'start', 
        'end', 
        'created_by',
        'tracker_id',
    )

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'tracker', 
        'tracker_id',
        'tracker_instance', 
        'tracker_instance_id',
        'question', 
        'display_answers',
        'answered_for',
        'created_at',
        'updated_at',
    )

@admin.register(TrackerGroup)
class TrackerGroup(admin.ModelAdmin):
    list_display = (
        'name', 
        'display_available_to',
        'created_at', 
        'updated_at',
        'active', 
        'created_by',
        'id',
    )

@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_display = (
        'name', 
        'question',
        'created_at', 
        'updated_at',
        'active', 
        'created_by',
    )



