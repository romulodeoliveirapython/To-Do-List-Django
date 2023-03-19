from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from .models import ToDo
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'todo/todo-list.html'
    model = ToDo
    context_object_name = 'todos'


class TodoDetailView(DetailView):
    model = ToDo
    template_name = 'todo/todo-detail.html'
    slug_url_kwarg = 'slug'