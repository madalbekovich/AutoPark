from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
]

if settings.DEBUG:
    urlpatterns += static('/static/', document_root = settings.STATIC_ROOT) + static('/media/', document_root = settings.MEDIA_ROOT)
