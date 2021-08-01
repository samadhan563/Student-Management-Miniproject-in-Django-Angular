import urllib
from django.core.mail import send_mail
import cv2
from django.views.decorators.csrf import csrf_exempt
import requests
from PIL import Image
import cloudinary
from deepface import DeepFace
from django.http.response import JsonResponse
from numpy.lib.type_check import imag
from rest_framework.parsers import JSONParser
from .serializer import LoginSerializer, UserProfileSerializer, UserSerializer
from .models import User, UserProfile
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
        user = User.objects.get(
            userName=data['userName'], password=data['password'])
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


@api_view(['POST'])
def upload(request):
    # print(request.data['files'])
    try:
        # data = JSONParser().parse(request)
        # print(data)
        # print(request.data['userName']+" "+request.data['password'])
        # return Response("ok  to upload")
        return Response(cloudinary.uploader.upload(request.data['files'])['url'])
    except:
        return Response("Failed to upload")


@api_view(['POST', 'GET'])
def userProfile(request, id):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['user'] = id
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Confirmation of Registration.',
                'Hi '+serializer.data['firstName'] +
                ', \n\t Welcome to python project, your rgistration is done successfully\n Thank You!',
                'samadhan563@gmail.com',
                [serializer.data['emaiId']]
            )
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)
    elif request.method == 'POST':
        user = UserProfile.objects.get(user=id)
        print(user)
        serializer = UserProfileSerializer(user, many=False)
        return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def imageMatch(request):
    data = JSONParser().parse(request)
    imgu1 = data['img1']
    imgu2 = data['img2']
    urllib.request.urlretrieve(imgu1,
                               "img1.jpg")
    urllib.request.urlretrieve(imgu2,
                               "img2.jpg")
    img1 = Image.open("img1.jpg")
    img2 = Image.open("img2.jpg")
    # img1 = img1.resize((900, 1200))
    # img2 = img2.resize((900, 1200))
    # img1 = cv2.imread(requests.get(imgu1))
    # img2 = cv2.imread(requests.get(imgu2))
    # img1 = cv2.imread(imgu1)
    # img2 = cv2.imread(imgu2)
    # cv2.imshow('image', img1)
    # print(img1)
    # img1="aaa"
    # print(img2)
    result = DeepFace.verify("img1.jpg", "img2.jpg")
    print(result['verified'])
    # obj = DeepFace.analyze(img_path=img2, actions=[
    #     'age', 'gender', 'race', 'emotion'])
    # print(obj)
    return Response("OK")
