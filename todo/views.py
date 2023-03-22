from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from todo.models import ToDo
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ToDoListView(ListView):
    template_name = 'todo/todo-list.html'
    model = ToDo
    context_object_name = 'todos'

    # Lógica para que o usuário consiga ver somente os objetos relacionados ao seu user
    def get_queryset(self):
        return ToDo.objects.filter(user = self.request.user)


@method_decorator(login_required, name='dispatch')
class TodoDetailView(DetailView):
    model = ToDo
    template_name = 'todo/todo-detail.html'
    slug_url_kwarg = 'slug'


@method_decorator(login_required, name='dispatch')
class ToDoUpdate(UpdateView):
    model: ToDo
    queryset: ToDo.objects.all()
    success_url = reverse_lazy('todo:list')
    template_name = 'todo-update.html'