from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    action = models.CharField(max_length=20, choices=[('line_count', 'Line Count'), ('word_count', 'Word Count')])
    result = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
