from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from example_api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_api.urls')),
    # path('file/', include('documents.urls')),
]
if settings.DEBUG is True:	
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +[
    path('admin/', admin.site.urls),
    path('event_api/', include('Event.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('file/', include('documents.urls')),
    path('', include('example_api.urls'))
    ]
  

