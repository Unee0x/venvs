from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Bin Codex',
        'title': 'First Blog Post',
        'content': 'Post content',
        'date_posted': 'July 7, 2017'
    },
    {
        'author': 'Unee0x Cee',
        'title': 'Second Blog Post',
        'content': 'Post content',
        'date_posted': 'July 9, 2017'
    },

]
def home(request):

    context = {
        'posts': posts
    }
    return render(request, '_blog/home.html', context)


def about(request):
    return render(request, '_blog/about.html', {'title': 'Django_Blog'})
