from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Data
from .serializers import StudentSerializers
#from rest_framework.views import APIView


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Data.objects.get(id = id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        stu = Data.objects.all()
        serializer = StudentSerializers(stu,many = True)
        return Response(serializer.data)
    

    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'your data has been created successfully'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = pk
        stu = Data.objects.get(id = id)
        serializer = StudentSerializers(stu,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'you data has been completely changed successfully'})
        return Response(serializer.errors) 
    
    if request.method == 'PATCH':
        id = pk
        stu = Data.objects.get(id = id)
        serializer = StudentSerializers(stu,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partical data has been updated successfully'})
        return Response(serializer.errors) 

    if request.method == 'DELETE':
        id = pk
        stu = Data.objects.get(pk = id)
        stu.delete()
        return Response({'msg':'you data has been delete...'})

