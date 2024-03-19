from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('category/', include('categories.urls')),
    path('project/', include('projects.urls')),
    path('schedule/', include('schedule.urls')),
    path('task/', include('tasks.urls')),
    path('team/', include('team.urls'))
]