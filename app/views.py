from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
# Create your views here.
@api_view(['GET'])
def tillu(request):
    object1= Student.objects.all()
    objectseriali = studentseriali(object1,many=True)
    return Response(objectseriali.data)

@api_view(['POST'])
def post(request):
    object2 = Student.objects.get()
    objectseriali = studentseriali(object2,data=request.data)
    return Response(objectseriali.data)


@api_view(['POST'])
def update(request,id):
    object2 = Student.objects.get(id=id)
    objectseriali = studentseriali(instance=object2,data=request.data)
    return Response(objectseriali.data)