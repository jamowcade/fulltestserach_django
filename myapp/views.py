from django.shortcuts import render
from .models import mylogs
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline

# Create your views here.


def index(request):
    logs = mylogs.objects.all()
    q = request.GET.get('search')

    if q:
        vector = SearchVector('name','description', 'port','http_response', 'ip_address')
        query = SearchQuery(q, search_type="raw")
        logs = mylogs.objects.annotate(search=vector).filter(search=query)
        print(logs)
    print(q)
    context = {
        "logs":logs
    }

    return render(request, 'index.html', context)