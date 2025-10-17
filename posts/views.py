from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostListView(ListView):
    """
    PostListView is going to retrive all of the objects formt the Post table in the data base
    """

    # template_name attribute is going to render a specific html file
    template_name = "posts/list.html"
    # model attribute is to let django know from which model we want to retrieve data
    model = Post
    # context_object_name will allow us to modify the name on how we call it inside of the html
    context_object_name = "posts"


class PostDetailView(DetailView):
    """

    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "detailed"
