from django.contrib import admin
from .models import UserInfo, ProfilePicture

# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_created')

admin.site.register(ProfilePicture)