from django.urls import path
from . import views
from .views import FileProcessingAPI,  index, result

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('process-file/', FileProcessingAPI.as_view(), name='process_file_api'),
    path('result/<int:file_id>/', result, name='result_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

