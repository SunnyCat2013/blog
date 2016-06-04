from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def home(request):
    return HttpResponse("Hello Django, agian. ??")


def detail(request, args):
    try:
        article_id = int(args) - 1
    except:
        return HttpResponse("Invalid Article Number...")

    article_list = Article.objects.all()
    if article_id not in range(len(article_list)):
        return HttpResponse("Invalid Article Number...")

    atc = Article.objects.all()[article_id]
    #return_str = 'Title:\t%s\nCategory:\t%s\nDate:\t%s\nContent:\n%s\n' % (atc.title, atc.category, atc.date_time, atc.content)
    #return HttpResponse(return_str)
    return render(request, 'show_atc.html', {'title':atc.title})
