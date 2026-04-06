from django.contrib import admin
from .models import CPPUser
class JobSeekerAdmin(admin.ModelAdmin):
    pass

class RecruiterAdmin(admin.ModelAdmin):
    pass

class CPPUserAdmin(admin.ModelAdmin):
    ordering = ['id', 'email', 'username']
    search_fields = ['email', 'username']
    model = CPPUser
    
# Register your models here.
admin.site.register(CPPUser, CPPUserAdmin)
