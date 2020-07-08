from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display =  [f.name for f in User._meta.fields]




admin.site.register(User, UserAdmin)