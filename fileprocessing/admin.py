from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'action', 'uploaded_at')
    readonly_fields = ('result', 'uploaded_at')
