# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):

    # posts = []

    posts = [
        {'id': 1, 'title':'First Post', 'body': 'This is my First Post'},
        {'id': 2, 'title':'Second Post', 'body': 'This is my Second Post'},
        {'id': 3, 'title':'Third Post', 'body': 'This is my Third Post'},
    ]
    return render(request, 'blog/index.html', {'posts': posts})

def show(request, id):
    posts = [
        {'id': 1, 'title': 'First Post', 'body': 'This is my First Post'},
        {'id': 2, 'title': 'Second Post', 'body': 'This is my Second Post'},
        {'id': 3, 'title': 'Third Post', 'body': 'This is my Third Post'},
    ]
    return render(request, 'blog/show.html', {'id': posts[int(id) - 1]})