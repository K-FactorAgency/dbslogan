from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, RedirectView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django import forms
from .models import Post


class IndexView(ListView):
    model = Post
    template_name = 'nemo/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class RegisterView(CreateView):
    template_name = 'nemo/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('nemo:login')


class LoginView(LoginView):
    template_name = 'nemo/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('nemo:index')


class LogoutView(LogoutView):
    next_page = reverse_lazy('nemo:index')


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'nemo/create_post.html'
    fields = ['content']
    success_url = reverse_lazy('nemo:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['content'].widget = forms.Textarea(attrs={'rows': 3})
        return form


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'nemo/delete_post.html'
    success_url = reverse_lazy('nemo:index')

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class LikePostView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('nemo:index')

    def get_redirect_url(self, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        user = self.request.user

        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        return super().get_redirect_url(*args, **kwargs)
