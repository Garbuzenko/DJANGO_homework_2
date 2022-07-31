from django.shortcuts import render, redirect
from django.urls import reverse

from PaginatorSingleton import PaginatorSingleton

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    paginator = PaginatorSingleton().getPaginator()
    current_page = int( request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
