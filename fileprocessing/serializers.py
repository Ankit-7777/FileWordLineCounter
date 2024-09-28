from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['file', 'action', 'result', 'uploaded_at']
        read_only_fields = ['result', 'uploaded_at']
