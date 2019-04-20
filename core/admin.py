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



admin.site.register(TrackerGroup)
admin.site.register(Answer)
admin.site.register(Response)
admin.site.register(TrackerGroupInstance)



