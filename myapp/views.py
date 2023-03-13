from django.shortcuts import render
from .models import mylogs
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    logs = mylogs.objects.all()
    per_page = 20
    obj_paginator = Paginator(logs, per_page)
    firt_page = obj_paginator.page(1).object_list
    page_range = obj_paginator.page_range
    # return JsonResponse({"logs":list(logs.values())})
    logs = mylogs.objects.all()
    context = {
        "first_page":firt_page,
        "logs":logs,
        'obj_paginator': obj_paginator,
        'page_range': page_range
    }
    if request.method == 'POST':
        #getting page number
        page_no = request.POST.get('page_no', None) 
        logs = list(obj_paginator.page(page_no).object_list.values('id', 'name','description','ip_address','port','http_response'))
        return JsonResponse({"logs":logs})
    return render(request, 'index.html', context)

def search(request):
    logs = mylogs.objects.all()
    q = request.GET.get('search')
    if q:
        print(q)
        vector = SearchVector('name','description', 'port','http_response', 'ip_address')
        query = SearchQuery(q, search_type="raw")
        # search_headline = SearchHeadline('description', query) 
        logs = mylogs.objects.annotate(search=vector).filter(search=query)
        return JsonResponse({"logs":list(logs.values())})

    return JsonResponse({"logs":list(logs.values())})
