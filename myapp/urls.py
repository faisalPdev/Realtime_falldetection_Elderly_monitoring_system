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
    path('search_caregiver/',views.search_caregiver),
    path('search_elderlyperson/',views.search_elderlyperson),
    path('logout/',views.logout),
    path('videolog/',views.videolog),

    # --------------------- fluttter Caregiver urls-------------------
    path('login_flutter/',views.login_flutter),
    path('view_allocated_elderly_person/', views.view_allocated_elderly_person),
    path('manual_alert/', views.manual_alert),
    path('communication/',views.communication_caregiver),
    path('medication_remainder_tracking/',views.medication_remainder_tracking),
    path('view_profile_caregiver/',views.view_profile_caregiver),
    path('change_password_flutter/',views.change_password_flutter),

    #---------------------------flutter  Elderly Person urls------------------
    path('view_allocated_caregiver/', views.view_allocated_elderly_person),
    path('sos_manual_alert/', views.sos_manual_alert),
    path('communication_elderlyperson/',views.communication_elderlyperson),
    path('medication_remainder/',views.medication_remainder),
    path('view_profile_elderlyperson/',views.view_profile_elderlyperson),


]

