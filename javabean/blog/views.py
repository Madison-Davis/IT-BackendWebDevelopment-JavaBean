# Imports
from django.shortcuts import render

posts = [
    {
        'author' : 'Corey Brunsk',
        'title' : 'Post: Brewing with Excitement',
        'content' : 'First Post Content',
        'date_post' : 'September 1, 2000'
    },
    {
        'author' : 'Dave Rodderham',
        'title' : "Post: Java's Delicious Delicacy",
        'content' : 'Second Post Content',
        'date_post' : 'September 2, 2000'
    }
]

# Functions
def home(request):
    context = {
        'post' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})