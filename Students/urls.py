from django.urls import path, include
from . import views

urlpatterns = [
    path('list-students/', views.listStudents, name="list-Student"),
    path('register-student/', views.registerStudent, name="register-Student"),
    path('update-student/<str:sk>', views.updateStudent, name="update-Student"),
    path('remove-student/<str:sk>', views.removeStudent, name="remove-Student"),
]