# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from todo.models import Alumno, Carrera
from todo.serializers import AlumnoSerializer, CarreraSerializer

# Create your views here.
@csrf_exempt
def alumno_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlumnoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def alumno_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        alumno = Alumno.objects.get(pk=pk)
    except Alumno.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AlumnoSerializer(alumno)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AlumnoSerializer(alumno, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        alumno.delete()
        return HttpResponse(status=204)

@csrf_exempt
def carrera_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        carreras = Carrera.objects.all()
        serializer = CarreraSerializer(carreras, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarreraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def carrera_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        carrera = Carrera.objects.get(pk=pk)
    except Carrera.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarreraSerializer(carrera)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarreraSerializer(carrera, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        carrera.delete()
        return HttpResponse(status=204)