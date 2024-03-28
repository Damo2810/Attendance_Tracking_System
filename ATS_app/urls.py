from django.urls import path
from . import views

#config url
urlpatterns = [
    # string url, function name
    # chop off the app url and sends the 
    # remaining part
    path('', views.home),
    path('login_as/', views.login_as, name='login_as'),
    path('student_login/', views.student_login, name='student_login'),   
    path('parent_login/', views.parent_login, name='parent_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('student_register/',views.student_register, name="student_register"),
    path('teacher_register/',views.teacher_register, name="teacher_register"),
    path('parent_register/',views.parent_register, name="parent_register"),
    path('Teacher_Dashboard/',views.teacher_dashboard, name="Teacher_Dashboard"),
    path('Student_Dashboard',views.student_dashboard, name="Student_Dashboard"),
    path('Parent_Dashboard',views.parent_dashboard, name="Parent_Dashboard"),
    path('attendance_entry/',views.attendance_entry, name='attendance_entry'),
    path('parent_upload/',views.PARENT_upload, name='parent_upload'),
    
]