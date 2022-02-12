from dataclasses import field
from msilib.schema import Class
from multiprocessing import context
from pyexpat import model
from re import template
from turtle import title
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.urls import reverse


from django.template.defaultfilters import slugify
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
# Create your views here.

def home_view(request, *args, **kwargs):
    # import pdb;pdb.set_trace()
    posts = Post.objects.filter(status="PUBLISHED")
    context_data = {
        "title": "HOME | POSTS",
        "posts": posts,
    }
    return render(request, "blog/index.html", context_data)

class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status="PUBLISHED")
    context_object_name = "posts"
    ordering = ["-modified_at"]
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["title"] = "Home Page | Posts"
        return data

post_list_view = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["title"] = "Post"
        return data

post_detail_view = PostDetailView.as_view()

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content', 'Summary','status', 'tags']

    def form_valid(self, form):
       form.instance.author=self.request.user
       form.instance.slug=slugify(form.instance.title)
       return super().form_valid(form)

post_create_view = PostCreateView.as_view()

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'Summary','status', 'tags']
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
       form.instance.author=self.request.user
       form.instance.slug=slugify(form.instance.title)
       return super().form_valid(form)

post_update_view = PostUpdateView.as_view()


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        

post_delete_view = PostDeleteView.as_view()

