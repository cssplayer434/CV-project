

# Register your models here.
from django.contrib import admin
from .models import CVTemplate, CV

@admin.register(CVTemplate)
class CVTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'active')

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'selected_template', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
