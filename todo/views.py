from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from todo.models import ToDo
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from todo.forms import ToDoForm


@method_decorator(login_required, name='dispatch')
class TodoCreateView(CreateView):
    model = ToDo
    form_class = ToDoForm
    template_name = 'todo/todo-create.html'
    success_url = reverse_lazy('todo:create')

    # Verifica se o user está autenticado. Caso não esteja, encaminha-o para a página de Login
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            return redirect('accounts:login')


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
class ToDoUpdateView(UpdateView):
    model: ToDo
    queryset: ToDo.objects.all()
    success_url = reverse_lazy('todo:list')
    template_name = 'todo/todo-update.html'

@method_decorator(login_required, name='dispatch')
class ToDoDeleteView(DeleteView):
    model = ToDo
    fields = '__all__'
    success_url = reverse_lazy('todo:list')
