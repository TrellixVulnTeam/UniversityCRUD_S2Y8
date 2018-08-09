from django.urls import path
from . import views


# add a namespace so Django can differentiate between apps in project so it knows
# exactly which is the correct view to create for a url when {% url %} is used
# this namespace will come right after url tag and before the 'name' of the view 
# for eg.: {% url 'uni:detail' ...
# app_name = 'uni'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /uni/123
    path('<slug:student_id_num>/', views.detail, name='detail'),
    #path('<slug:student_id_num>/', views.summary, name='summary'),
]