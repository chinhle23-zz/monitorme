from django.contrib import admin
from core.models import User

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    name_display = ('name')
    fields = ['name']
