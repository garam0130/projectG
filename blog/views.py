from django.shortcuts import render, redirect
from django.http import Http404
from blog.models import Spot, Activity

def index(request):
    spot_list = Spot.objects.all()
    activity_list = Activity.objects.all()
    return render(request, 'blog/index.html', {
        'spot_list' : spot_list,
        'first_spot' : spot_list[0],
        'activity_list' :activity_list,
    })

def travel(request):
    spot_list = Spot.objects.all().order_by('-date', 'name')
    return render(request, 'blog/travel.html', {
        'spot_list' : spot_list,
        'first_spot' : spot_list[0],

    })


def year(request, value):
    try:
        year_value = int(value)
    except ValueError:
        redirect('/')
    spot_list = Spot.objects.filter(date__year=year_value).order_by('date', 'name')
    return render(request, 'blog/travel.html', {
        'spot_list' : spot_list,
        'first_spot' : spot_list[0],
        })