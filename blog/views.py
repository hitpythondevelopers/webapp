from django.shortcuts import render
from .models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', 
    {'categories': Category.objects.all(), 'posts': Blog.ojects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })