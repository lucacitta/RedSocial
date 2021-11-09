from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('career/', include('apps.career.api.urls')),
    path('courses/', include('apps.courses.api.urls')),
    path('professor/', include('apps.professor.api.urls'))
]
