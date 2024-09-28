from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from .forms import FileUploadForm  
from collections import Counter
import re

def count_lines(content):
    lines = content.splitlines()
    return len([line for line in lines if line.strip()])

def count_words(content):
    words = re.findall(r'\b\w+\b', content.lower())
    filtered_words = [word for word in words if word not in {'and', 'the', 'a', 'in', 'on'}]
    return Counter(filtered_words)

class FileProcessingAPI(APIView):
    def post(self, request):
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            file_instance = serializer.save()
            
            try:
                content = file_instance.file.read().decode('utf-8', errors='ignore')
            except Exception as e:
                return Response({'error': 'Unable to read file content.'}, status=status.HTTP_400_BAD_REQUEST)
            
            if file_instance.action == 'line_count':
                result = count_lines(content)
            elif file_instance.action == 'word_count':
                result = count_words(content)

            file_instance.result = str(result)
            file_instance.save()

            return redirect('result_page', file_instance.id)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        files = UploadedFile.objects.all()
        serializer = UploadedFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def index(request):
    form = FileUploadForm()
    return render(request, 'fileprocessing/index.html', {'form': form})

def result(request, file_id):
    file_instance = UploadedFile.objects.get(id=file_id)
    return render(request, 'fileprocessing/result.html', {
        'result': file_instance.result,
        'action': file_instance.action
    })
