"""
URL configuration for myFirst project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from . import hello

urlpatterns = [
    path('', hello.index, name= 'index'),
    path('vision/', hello.vision, name='ccmsvision'),
    path('mission/', hello.mission, name='ccmsmission'),
    path('objectives/', hello.objectives, name='ccmsobjectives'),
    path('admin/', admin.site.urls),
]
