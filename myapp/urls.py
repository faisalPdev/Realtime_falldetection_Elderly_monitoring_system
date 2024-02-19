"""
URL configuration for Real_time_fall_detetion project.

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
from django.urls import path, include

from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/',views.login),
    path('login_post/', views.login_post),
    path('add_caregiver/', views.add_caregiver),
    path('add_caregiver_post/', views.add_caregiver_post),
    path('add_allocation/<cid>', views.add_allocation),
    path('add_allocation_post/',views.add_allocation_post),
    path('add_elderlyperson/', views.add_elderlyperson),
    path('add_elderlyperson_post/', views.add_elderlyperson_post),
    path('change_password/', views.change_password),
    path('change_password_post/', views.change_password_post),
    path('view_caregiver/', views.view_caregiver),
    path('view_allocated/', views.view_allocated),
    path('view_elderlyperson/', views.view_elderlyperson),
    path('admin_home/',views.admin_home),
    path('edit_elderlyperson/<id>', views.edit_elderlyperson),
    path('edit_elderlyperson_post/', views.edit_elderlyperson_post),
    path('edit_caregiver/<id>', views.edit_caregiver),
    path('edit_caregiver_post/', views.edit_caregiver_post),
    path('delete_caregiver/<id>',views.delete_caregiver),
    path('delete_elderlyperson/<id>', views.delete_elderlyperson),

]

