from django.urls import path
from . import views


# add a namespace so Django can differentiate between apps in project so it knows
# exactly which is the correct view to create for a url when {% url %} is used
# this namespace will come right after url tag and before the 'name' of the view 
# for eg.: {% url 'uni:detail' ...
# app_name = 'uni'

urlpatterns = [

    # ----------- STUDENTS URLs ----------- #
    path('students/', views.students_index, name='students_index'),
    # ex: /uni/123
    path('students/<slug:student_id_num>/', views.students_detail, name='students_detail'),
    path('students/<slug:student_id_num>/', views.students_delete, name='students_delete'),

    # ----------- DISCIPLINES URLs ----------- #
    path('disciplines/', views.disciplines_index, name='disciplines_index'),
    path('disciplines/<int:id>/', views.disciplines_detail, name='disciplines_detail'),
    path('disciplines/create', views.disciplines_create, name='disciplines_create'),
    
    # ----------- TEACHERS URLs ----------- #
    path('teachers/', views.teachers_index, name='teachers_index'),
    path('teachers/<slug:teacher_id_number>/', views.teachers_detail, name='teachers_detail'),


    
]