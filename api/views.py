from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserDb
from .serializers import UserSerializer
from rest_framework import status
from .mypagination import MyPageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView



class UserList(ListCreateAPIView):
    queryset=UserDb.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = '__all__'

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def user_api(request, pk=None):
    if request.method == 'GET':
        id=pk
        if id is not None:
            user=UserDb.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='PUT':
        id=pk
        user=UserDb.objects.get(pk=id)
        serialzer = UserSerializer(user, data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'msg':"Data Successfully Updated"})
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='PATCH':
        id=pk
        user=UserDb.objects.get(pk=id)
        serialzer = UserSerializer(user, data=request.data, partial=True)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'msg':"Partial Data Successfully Updated"})
        return Response(serialzer.errors)

    if request.method == 'DELETE':
        id=pk
        user=UserDb.objects.get(pk=id)
        user.delete()
        return Response({'msg':'Data Deleted'})


#***********************************************************************************
 # elif id is None:
        #     paginator = MyPageNumberPagination()
        #     user=UserDb.objects.all()
        #     result_page = paginator.paginate_queryset(user, request)
        #     serializer=UserSerializer(result_page, many=True)
        #     return paginator.get_paginated_response(serializer.data)