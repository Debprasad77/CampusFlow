from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from student_management_system import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_management_app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

