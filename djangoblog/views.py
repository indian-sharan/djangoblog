from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
#def home(request):
 #   return render(request, 'home.html', {})

 # class based

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-create_date']

class ArticleView(DetailView):
    model = Post
    template_name = 'details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    #fields = ('title', 'body')