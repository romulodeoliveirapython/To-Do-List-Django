from django.urls import path
from todo.views import IndexView, TodoDetailView


app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('detail/<uuid:pk>/', TodoDetailView.as_view(), name = 'detail'),
]
