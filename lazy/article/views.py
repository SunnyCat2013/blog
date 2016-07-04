from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from article.models import Article

import socket

## change article text to html
from markdown import markdown

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    #return HttpResponse("Hello Django, agian. ??")
    return_dict = {'blog_list': Article.objects.all()}
    return HttpResponse(template.render(return_dict, request))


def detail(request, args):
    # detect if args is well-format

    try:
        article_id = int(args)
    except:
        return HttpResponse("Invalid Article Number...")

    article_list = Article.objects.all()
    if article_id not in range(1, len(article_list)+1):
        return HttpResponse("Invalid Article Number...")

    atc = Article.objects.get(id=article_id)
    template = loader.get_template('show_atc.html')

    # show markdown text
    #mfile = open('./../../django-markdown-deux.md', 'r').read()
    #mfile = open('/Users/cslzy/python/Django/django-markdown-deux.md', 'r').read()
    #atc.content = mfile

    urlPath = request.path

    if socket.gethostname() == 'localhost':
        urlPath = 'http://127.0.0.1:8000' + urlPath
    else:
        urlPath = 'http://www.sofamiri.com' + urlPath

    return_dict = {'post':atc, 'full_url': urlPath}
    return HttpResponse(template.render(return_dict, request))
    #return HttpResponse(markdown(atc.content).encode('utf8'))
    

def atc_list(request):
    # detect if args is well-format
    return HttpResponse("test article list...")


