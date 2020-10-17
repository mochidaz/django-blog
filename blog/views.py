from django.shortcuts import render
from django.db.models import Q

from article.models import Article

def IndexView(request):
    post = Article
    introduction = post.objects.filter(title="Perkenalan")
    newest = post.objects.all().order_by('-date')[0:4]
    return render(request, 'main/index.html', {'perkenalan':introduction, 'terbaru':newest})

def SearchView(request):
    q = request.GET.get('q', None)        
    post = Article
    queryset = post.objects.filter(Q(title__icontains=q) | Q(category__icontains=q))

    return render(request, 'blog/search.html', {'result':queryset, 'q':q})
