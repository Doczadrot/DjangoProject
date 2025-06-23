from django.urls import path
from .views import *
from students import views

app_name = 'students' #Название приложения для ссылки
urlpatterns = [
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('example/', example_view, name='example'),
    path('home/', views.home, name='home'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student_list/', views.student_list, name='student_list'),
    path('mymodel/list/', views.MyModelList.as_view(), name='mymodel_list'),
    path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
]