from django.contrib import admin
from .models import User, Profile

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','user_id')

# class CustomerUserAdmin(UserAdmin):
#     inlines = (ProfileInline,)

admin.site.register(User, UserAdmin)
admin.site.register(Profile)

# admin.site.unregister(User)
# admin.site.register(User, CustomerUserAdmin)