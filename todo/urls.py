from django.urls import path
from todo.views import ToDoListView, TodoDetailView, ToDoUpdateView


app_name = 'todo'

urlpatterns = [
    path('', ToDoListView.as_view(), name = 'list'),
    path('detail/<uuid:pk>/', TodoDetailView.as_view(), name = 'detail'),
    path('update/<uuid:pk>/', ToDoUpdateView.as_view(), name = 'update')
]
