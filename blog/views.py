from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import my_blogs


def show_blog(request):
    return render(request, "my_blogs.html", {"my_blogs": my_blogs})


def get_blog(request, blog_id):
    try:
        return HttpResponse(my_blogs[int(blog_id)][0]+my_blogs[int(blog_id)][1])
    except IndexError:
        raise Http404("We don't have any.")

