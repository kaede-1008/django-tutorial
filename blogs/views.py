from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.

class IndexView(ListView):
    model = Post
    paginate_by = 5
    ordering = ['-update_at']
    template_name = 'blogs/index.html'

class DetailView(DetailView):
    model = Post
    template_name = 'blogs/detail.html'
 
 
class CreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'blogs/create.html'
 
 
class UpdateView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blogs/update.html'
 
 
class DeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:index')
    template_name = 'blogs/delete.html'