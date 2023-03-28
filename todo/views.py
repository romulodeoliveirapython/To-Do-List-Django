from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from todo.models import Tasks
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from todo.forms import ToDoForm


@method_decorator(login_required, name='dispatch')
class TodoCreateView(CreateView):
    model = Tasks
    form_class = ToDoForm
    template_name = 'todo/todo-create.html'
    success_url = reverse_lazy('todo:list')

    # Verifica se o user está autenticado. Caso não esteja, encaminha-o para a página de Login
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            return redirect('login')


@method_decorator(login_required, name='dispatch')
class ToDoListView(ListView):
    template_name = 'todo/todo-list.html'
    model = Tasks
    context_object_name = 'todo'

    # Lógica para que o usuário consiga ver somente os objetos relacionados ao seu user
    def get_queryset(self):
        return Tasks.objects.filter(user = self.request.user).order_by('title')


@method_decorator(login_required, name='dispatch')
class TodoDetailView(DetailView):
    model = Tasks
    template_name = 'todo/todo-detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'todo'


@method_decorator(login_required, name='dispatch')
class ToDoUpdateView(UpdateView):
    model = Tasks    
    form_class = ToDoForm
    success_url = reverse_lazy('todo:list')
    template_name = 'todo/todo-update.html'
    context_object_name = 'todo'


@method_decorator(login_required, name='dispatch')
class ToDoDeleteView(DeleteView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('todo:list')
    context_object_name = 'todo'
