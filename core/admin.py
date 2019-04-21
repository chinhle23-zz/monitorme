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
        'active'
    )

@admin.register(TrackerGroupInstance)
class TrackerGroupInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'tracker', 
        'start', 
        'end', 
        'created_by'
    )

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'tracker', 
        'tracker_instance', 
        'question', 
        'display_answers',
        'answered_for',
        'created_at',
        'updated_at'
    )

admin.site.register(TrackerGroup)
admin.site.register(Answer)



