from django.views.generic import View
from todo.models import ToDo
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ToDoListView(ListView):
    template_name = 'todo/todo-list.html'
    model = ToDo
    context_object_name = 'todos'


@method_decorator(login_required, name='dispatch')
class TodoDetailView(DetailView):
    model = ToDo
    template_name = 'todo/todo-detail.html'
    slug_url_kwarg = 'slug'