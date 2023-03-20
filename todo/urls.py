from django.urls import path
from todo.views import ToDoListView, TodoDetailView


app_name = 'todo'

urlpatterns = [
    path('', ToDoListView.as_view(), name = 'list'),
    path('detail/<uuid:pk>/', TodoDetailView.as_view(), name = 'detail'),
]
