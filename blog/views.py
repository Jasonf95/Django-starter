from django.shortcuts import render

posts = [
    {
       'author': 'Erfan_fekri',
       'title':  'Blog post 1',
       'content': 'A brave start',
       'date_posted': 'APR 12, 2024'
    },
    {
       'author': 'Ariana Grande',
       'title':  'Blog post 2',
       'content': 'Eternal sunshine is out now!',
       'date_posted': 'APR 11, 2024'

    }
]


def homepage(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def aboutpage(request):
    return render(request, 'blog/about.html', {'title': 'About'})