from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from article.models import Article

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
    return_dict = {'title': atc.title, 'category': atc.category, 'date': atc.date_time, 'content': atc.content}
    return HttpResponse(template.render(return_dict, request))
