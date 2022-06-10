from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializers import EmployeesSerializer, EmployeesTreeSerializer
from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

# def show_employees(request):
#     return render(request, "catalog/employees.html", {'employees': Employee.objects.all()})

class EmployeeViewSet(ModelViewSet):

    # queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['full_name', 'position', 'salary', 'employment_date', 'parent']
    search_fields = ['full_name', 'position', 'salary']

    ordering_fields = ['full_name', 'position', 'salary', 'employment_date']


class EmployeeTreeViewSet(ModelViewSet):

    # queryset = Employee.objects.all()

    permission_classes = [IsOwnerOrReadOnly]

    queryset = Employee.objects.root_nodes()
    serializer_class = EmployeesTreeSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['full_name', 'position', 'salary', 'employment_date', 'parent']
    search_fields = ['full_name', 'position', 'salary']

    ordering_fields = ['full_name', 'position', 'salary', 'employment_date']



