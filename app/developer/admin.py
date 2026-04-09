from django.contrib import admin
from .models import DatabaseFile

class DatabaseFileAdmin(admin.ModelAdmin):
    ordering = ['id', 'name']
    search_fields = ['name']
    model = DatabaseFile
    
# Register your models here.
admin.site.register(DatabaseFile, DatabaseFileAdmin)
