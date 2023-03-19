from django.shortcuts import render
from django.views.generic import View
from .models import ToDo


"""
class IndexView(View):
    template_name = 'todo/index.html'
    http_method_names = ['get']

    def get(self, request):
        return render(request, self.template_name) 
"""

class IndexView(View):
    template_name = 'todo/todo-list.html'
    http_method_names = ['get']
    model = ToDo

    def get(self, request):
        # Recupera todos os objetos da model ToDo
        todos = self.model.objects.all()

        # Passa os objetos para o template usando o contexto
        context = {'todos': todos}
        return render(request, self.template_name, context)