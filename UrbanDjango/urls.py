"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from task2.views import Index_class, func_index
# from task3.views import start_index, buy_index, cart_index
from task1.views import start_index, buy_index, cart_index
from task1.views import sign_up_by_django, news_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_index),
    path('buy/', buy_index),
    path('cart/', cart_index),
    path('registration/', sign_up_by_django),
    path('news/', news_index)
]
