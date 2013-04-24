from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from Blog.models import Article, Category
from django.template import RequestContext


articles = Article.objects.order_by('date').reverse()[:5]
categories = Category.objects.all();
default = {'articles':articles, 'categories': categories}

def     home(request):
    return render(request, 'blog/default.html', default)

def     view_article(request, id_article, slug = None):
    article = get_object_or_404(Article, id=id_article)
    default['article'] = article
    return render(request, 'blog/article.html', default)


def     view_category(request, id_category, slug = None):
    article = Article.objects.filter(category=id_category).order_by('date').reverse()
    default['content'] = article
    return render(request, 'blog/category.html', default)

def     view_archive(request):
    article = Article.objects.all().reverse()
    default['content'] = article
    return render(request, 'blog/archive.html', default)
    
