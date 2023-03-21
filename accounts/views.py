from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login


# Create your views here.
class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        # Coletar dados do formulário
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        # Chamar o método form_valid() da superclasse para salvar o objeto do formulário
        response = super().form_valid(form)

        # Autenticar o usuário
        user = authenticate(username=username, password=password)
        login(self.request, user)

        # Retornar a resposta da superclasse (redirecionamento para a página de sucesso)
        return response