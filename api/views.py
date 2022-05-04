from django.shortcuts import render, HttpResponse
from .models import RadiDept
from .serializers import RadiDeptSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import APIView


class RadiDeptList(APIView):

    def get(self, request):
        dept = RadiDept.objects.all()
        serializer = RadiDeptSerializer(dept, many=True)  # many=True because we are serializing a qs
        return Response(serializer.data)

    def get(self, request):
        serializer = RadiDeptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RadiDeptDetail(APIView):

    def get_object(self, id):
        try:
            return RadiDept.objects.get(pk=id)
        except RadiDept.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        dept = self.get_object(id)
        serializer = RadiDeptSerializer(dept)
        return Response(serializer.data)

    def put(self, request, id):
        dept = self.get_object(id)
        serializer = RadiDeptSerializer(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        dept = self.get_object(id)
        dept.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


'''
@api_view(['GET', 'POST'])
def radi_dept_list(request):
    if request.method == 'GET':                 # => READ ALL
        dept = RadiDept.objects.all()
        serializer = RadiDeptSerializer(dept, many=True)    # many=True because we are serializing a qs
        return Response(serializer.data)    #

    if request.method == 'POST':
        serializer = RadiDeptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=statux.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def radi_dept_detail(request, pk):
    try:
        dept = RadiDept.objects.get(pk=pk)
    except RadiDept.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':             # => READ SINGLE
        serializer = RadiDeptSerializer(dept)
        return Response(serializer.data)

    elif request.method == 'PUT':           # => UPDATE
        serializer = RadiDeptSerializer(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':        # => DELETE
        dept.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)     # Meaning no content
'''

