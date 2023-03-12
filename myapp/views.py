from django.shortcuts import render
from .models import mylogs
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline
from django.http import JsonResponse
# Create your views here.

def index(request):
    logs = mylogs.objects.all()

    q = request.GET.get('search')
    if q:
        print(q)
        vector = SearchVector('name','description', 'port','http_response', 'ip_address')
        query = SearchQuery(q, search_type="raw")
        # search_headline = SearchHeadline('description', query) 
        logs = mylogs.objects.annotate(search=vector).filter(search=query)
        return JsonResponse({"logs":list(logs.values())})
        print(logs)
    # return JsonResponse({"logs":list(logs.values())})
    logs = mylogs.objects.all()
    print(q)
    context = {
        "logs":logs
    }
    
    return render(request, 'index.html', context)

def testAjax(request):
    val = request.GET.get('search')
    print(val)
    logs = mylogs.objects.all()

    return JsonResponse({"logs":list(logs.values())})
