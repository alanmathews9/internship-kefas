"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home.views import (get_logs, create_logs, update_logs)
from django.views.decorators.csrf import csrf_exempt
from home.views import LogsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fn/home/', get_logs),
    path('home/create/', csrf_exempt(create_logs)),
    path('home/update/', csrf_exempt(update_logs)),
    path('home/', csrf_exempt(LogsView.as_view())),
] 