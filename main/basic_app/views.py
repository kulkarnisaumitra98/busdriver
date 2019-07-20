from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import random
from .models import Trackie, Tracker, PolyLine, Busdriver
# Create your views here.

flag = False
j = 99
polyLine = PolyLine.objects.all()


def getBusLocationDec(request):
    if request.is_ajax():
        # trackie = Trackie.objects.all()[0]
        # trackie.latitude -= 0
        # trackie.longitude -= 0
        # trackie.save()
        global j
        j -= 1

        if j == 0:
            j = 99

        return JsonResponse({"latitude": polyLine[j].latitude, "longitude": polyLine[j].longitude})


def getPolyLine(request):
    if request.is_ajax():
        global flag
        if flag:
            return JsonResponse({"Status": "fucked"})
        body_unicode = request.body.decode('utf-8')
        Postobject = json.loads(body_unicode)
        print(Postobject)
        for i in Postobject:
            polyob = PolyLine(latitude=i["latitude"], longitude=i["longitude"])
            polyob.save()

        flag = True

        return JsonResponse({"Status": "fucked"})


def postBusDriverLocation(request):
    if request.is_ajax():
        body_unicode = request.body.decode('utf-8')
        Postobject = json.loads(body_unicode)
        print(Postobject)
        busDriver = Busdriver(latitude=Postobject["latitude"], longitude=Postobject["longitude"])
        busDriver.save()

        return JsonResponse({"status": 200})
