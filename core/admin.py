from django.contrib import admin
from core.models import User, TrackerGroup, Question, Answer, Response

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
    exclude= ('slug', 'password',)

admin.site.register(TrackerGroup)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Response)



