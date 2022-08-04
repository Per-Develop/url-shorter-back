from urllib import request
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Addr
from .serializers import AddrSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import random
import string

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def index(request, value=None):
    obj= Addr.objects.filter(shortaddr=value).latest('date')
    print(obj.longaddr)
    return redirect(obj.longaddr)


def fetch(request):
    if request.method == 'POST':
        print(request.POST['addr'])
        ranca = random_char(5)
        Addr.objects.create(longaddr=request.POST['addr'], shortaddr=ranca)
        return render(request, 'insert.html',{'ranca': 'http://127.0.0.1:8000/'+ranca, 'zrix': 'https://zrix.ir/'+ranca})
    return render(request, 'insert.html')


class AddrListApiView(APIView):

    def get(self, request,value):
        addresses= Addr.objects.filter(shortaddr = value)
        serializer = AddrSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        ran = random_char(5)
        if Addr.objects.filter(shortaddr = ran).count() < 1:

            data = {
                'longaddr': request.data.get('longaddr'), 
                'shortaddr': ran, 
            }
            serializer = AddrSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            AddrListApiView.post(self, request)