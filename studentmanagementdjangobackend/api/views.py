

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .serializer import LoginSerializer, UserSerializer
from .models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'User': 'user-new',
#         'list':'list',
#     }
#     return Response(api_urls)

@api_view(['GET'])
# @apiOverview(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getById(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addNewUser(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PUT'])
def updateUser(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(f"User Nor found with id {id} ")
    data = JSONParser().parse(request)
    serializer = UserSerializer(instance=user, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def deleteById(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, many=False)
        user.delete()
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(f"User Nor found with id {id} ")


@api_view(['POST'])
def signIn(request):
    try:
        data = JSONParser().parse(request)
        print(data)
        user = User.objects.get(userName=data['userName'], password=data['password'])
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
        # userlog = LoginSerializer(data=data)
        # if userlog.is_valid():
            # user = User.objects.get(userName=userlog.data['userName'], password=userlog.data['password'])
            # serializer = UserSerializer(user, many=False)
            # return Response(serializer.data)
    except User.DoesNotExist:
        return Response(f"User Nor found with id ")


@api_view(['GET'])
def signIn1(request):
    try:
        user = User.objects.get(userName="Samadhan563", password="sama#0904")
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(f"User Nor found with id ")
