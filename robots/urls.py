from django.urls import path

from robots.views import new_robot_created

urlpatterns = [
    path('new_robot/', new_robot_created, name='Добавить запись о создании нового робота'),
]