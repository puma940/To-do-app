from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('uncomplete/<todo_id>', views.uncompleteTodo, name='uncomplete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deletealltodo', views.deleteAllTodo, name='deletealltodo'),
]
