from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rest-framework/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('accounts/', include('accounts.urls', namespace='accounts'))
]

from django.conf.urls.static import static
from . import settings

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)