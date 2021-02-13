import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from company.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls')),
    path('', include('users.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = page_not_found
