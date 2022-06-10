from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializers import EmployeesSerializer, EmployeesTreeSerializer
from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True


        return obj.owner == request.user


class EmployeeViewSet(ModelViewSet):


    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Employee.objects.all().prefetch_related('employee')
    serializer_class = EmployeesSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['full_name', 'position', 'salary', 'employment_date', 'parent']
    search_fields = ['full_name', 'position', 'salary']

    ordering_fields = ['full_name', 'position', 'salary', 'employment_date']

    def get_paginated_response(self, data):
       return Response(data)


class EmployeeTreeViewSet(ModelViewSet):


    permission_classes = [IsOwnerOrReadOnly]

    queryset = Employee.objects.root_nodes().prefetch_related('employee')
    serializer_class = EmployeesTreeSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['full_name', 'position', 'salary', 'employment_date', 'parent']
    search_fields = ['full_name', 'position', 'salary']

    ordering_fields = ['full_name', 'position', 'salary', 'employment_date']



