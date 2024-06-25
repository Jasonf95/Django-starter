from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from blog.models import Post

# Create your views here.


def home(response):
    return HttpResponse('<h>Hey, welcome to customer service\'s home page')


class BlogList(ListView):
    model = Post
    template_name = 'customer_service/home.html'
    context_object_name = 'posts'

