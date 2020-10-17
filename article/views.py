from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import resolve
from django.core.paginator import Paginator

from .models import Article

class PostView(ListView):
    model = Article
    paginate_by = 5
    results = model.objects.order_by('-date')
    template_name = 'blog/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.results, self.paginate_by)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)

        return context

def CategoryView(request, category):
    model = Article.objects.all().filter(category=category)
    paginator = Paginator(model, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/category.html', {'posts':model, 'category':category, 'page_obj':page_obj})

def PostDetail(request, category, slug):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Article,category=category, slug=slug)

    return render(request, template_name, {"post":post})


