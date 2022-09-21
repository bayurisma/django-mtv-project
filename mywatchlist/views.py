from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

mhs_name = 'Maulana Bayu Risma Santoso Sari'
studentID = 2106750401

def show_watchlist(req):
    data_watchlist = MyWatchList.objects.all()
    watched = list(filter(lambda x: x.watched == True, data_watchlist))
    context  = {
        'name' : mhs_name,
        'studentID': studentID,
        'watchlist': data_watchlist,
        'watched': len(watched),
        'unwatched': len(data_watchlist) - len(watched)
    }
    print(watched)
    return render(req, 'watchlist.html', context)

def show_xml(req):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(req):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

