from django.contrib import admin
from django.urls import path, include
from resolver import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Index'),
    path('jobsource', views.job_source, name='Job Source')
]
