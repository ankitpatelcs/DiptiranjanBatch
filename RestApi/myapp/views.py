from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def GetAllEmployees(request):
    users = User.objects.all()

    serial = Userserial(users,many=True)
    return Response(serial.data)

@api_view(['GET'])
def one_data(request,pk):    
    users = User.objects.get(id=pk)

    serial = Userserial(users)
    return Response(serial.data)

@api_view(['POST'])
def create_data(request):
    serial = Userserial(data=request.data)

    if serial.is_valid():
        serial.save()

        return Response(serial.data)

@api_view(['GET','PUT'])
def update_data(request,pk):
    user = User.objects.get(id=pk)
    if request.method == 'PUT':
        serial = Userserial(instance=user,data=request.data)

        if serial.is_valid():
            serial.save()

            return Response(serial.data)

    serial = Userserial(user)
    return Response(serial.data)

@api_view(['DELETE','GET'])
def delete_data(request,pk):
    try:
        user = User.objects.get(id=pk)
        if request.method == 'DELETE':
            try:
                user.delete()
                return Response('Data Deleted')
            except:
                return Response('Data not Found')
        serial = Userserial(user)
        return Response(serial.data)
    except:
        return Response('Invalid Id')