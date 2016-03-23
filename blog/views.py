from django.shortcuts import render
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
