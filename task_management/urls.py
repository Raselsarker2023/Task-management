from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('accounts.urls')),
    path('api/category/', include('categories.urls')),
    path('api/project/', include('projects.urls')),
    path('api/schedule/', include('schedule.urls')),
    path('api/task/', include('tasks.urls')),
    path('api/team/', include('team.urls'))
]