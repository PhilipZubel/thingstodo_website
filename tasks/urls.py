from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('report/<str:task_type>/', views.tasks, name='tasks'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('set_completed/<int:task_id>', views.set_completed, name="set_completed"),
    path('set_incomplete/<int:task_id>', views.set_incomplete, name="set_incomplete"),
]
