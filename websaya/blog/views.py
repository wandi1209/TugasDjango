from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from .models import Artikel

def blog_index(request):
    post = Artikel.objects.all()
    context = {
        'post' : post
    }
    return render(request, 'index.html', context)

class BlogClass(ListView):
    model = Artikel
    template_name = 'index1.html'