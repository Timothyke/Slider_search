from django.shortcuts import render
from .models import Slider, Blog
from django.db.models import Q

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    return render(request, 'index.html', {'slider': sliders})


def search(request):
    query = request.GET.get('query')
    if query:
        blogs = Blog.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query))

        return render(request, 'search.html', {'data': blogs, 'query': query})
    return render(request, 'search.html')
