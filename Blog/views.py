from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from Blog.models import *
from django.template import RequestContext
from Blog.forms import *

articles = Article.objects.order_by('date').reverse()[:5]
categories = Category.objects.all();
default = {'articles':articles, 'categories': categories}

def     home(request):
    return render(request, 'blog/default.html', default)

def     view_article(request, id_article, slug = None):
    article = get_object_or_404(Article, id=id_article)
    default['comments'] = Comment.objects.filter(article=article).order_by('date')
    default['article'] = article
    if request.method == 'POST':
        default['form'] = CommentForm(request.POST)
        if default['form'].is_valid():
            author =  default['form'].cleaned_data['author']
            content = default['form'].cleaned_data['content']
            new_comment = Comment(author=author, content=content, article=(Article.objects.get(id=1)))
            new_comment.save()
            #pas de javascript
            return HttpResponseRedirect("/article/"+id_article+"-"+slug)
    else:
        default['form'] = CommentForm()
    return render_to_response('blog/article.html', default, context_instance=RequestContext(request))

def     get_comment(request, id_article):
    article = get_object_or_404(Article, id=id_article)
    comment = Comment.objects.filter(article=article).order_by('date')    
    print id_article
    return render_to_response('blog/comments.html', {"comments":comment}, context_instance=RequestContext(request))

def     view_category(request, id_category, slug = None):
    article = Article.objects.filter(category=id_category).order_by('date').reverse()
    default['content'] = article
    return render(request, 'blog/category.html', default)

def     view_archive(request):
    article = Article.objects.all().reverse()
    default['content'] = article
    return render(request, 'blog/archive.html', default)


def     view_gallery(request, id_category, slug):
    cat = get_object_or_404(FileCategory, id=id_category)
    images = FileUpload.objects.filter(category=id_category)
    default['images'] = images
    return render(request, 'blog/gallery.html', default)
