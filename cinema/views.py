from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class MovieListView(APIView):
    def get(self, request, format=None):
        service = MovieModels.objects.all()
        serializer = MovieSerializers(service, many=True)
        return JsonResponse({
            "data": serializer.data,
            "success": True,
            "message": "Sent successfully !!!",
        }, status=200)


@api_view(['GET'])
def FilmsListView(request):
    if request.method == 'GET':
        snippets = MovieModels.objects.filter(is_active=True, category='films')
        serializer = MovieSerializers(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def FilmStartWithListView(request, startwith):
    if request.method == 'GET':
        snippets = MovieModels.objects.filter(is_active=True, category='films', title__startwith=startwith)
        serializer = MovieSerializers(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def MoviesDetailView(request, id):
    try:
        user = get_object_or_404(MovieModels, id=id, is_active=True)
    except MovieModels.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializers(user)
        return JsonResponse({
            "success": True,
            "data": serializer.data
        }, status=200)


class MoviesCreateView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = MovieSerializers
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "success": True,
                "message": "Sent successfully !!!",
                "data": serializer.data
                }, status=200)
        else:
            return JsonResponse({
                "success": False,
                "message": "Sent unsuccessfully !!!",
                }, status=400)
