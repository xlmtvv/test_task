from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializers import EmployeesSerializer

# def show_employees(request):
#     return render(request, "catalog/employees.html", {'employees': Employee.objects.all()})

class EmployeeViewtSet(ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer



