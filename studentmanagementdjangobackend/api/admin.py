from .models import User
from django.contrib import admin

# Register your models here.
# admin.site.register(User)
@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_filter=('userName','role')
    list_display=('userName','password','role')