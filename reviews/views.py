# from django.conf import settings
from django.shortcuts import render

def index(request):
    # if settings.DEBUG:
    #     import ipdb; ipdb.set_trace()
    name = request.GET.get("name") or "unknown"
    # return HttpResponse("Hey there, {}!".format(name))
    return render(request, "base.html", { "name": name })

def search(request):
    query = request.GET.get("query")
    return render(request, "search.html", { "query": query })