"""projectacc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',views.insert_topic,name='insert_topic'),
    path('insert_webpage/',views.insert_webpage,name='insert_webpage'),
    path('select_topic/',views.select_topic,name='select_topic'),
    path('delete_webpage/',views.delete_webpage,name='delete_webpage'),
    path('multi_selected/',views.multi_selected,name='multi_selected'),
    path('checkbox/',views.checkbox,name='checkbox'),
]
