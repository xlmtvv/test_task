from django.shortcuts import render
from .models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeesListSerializer, EmployeesDetailSerializer


def show_employees(request):
    return render(request, "catalog/employees.html", {'employees': Employee.objects.all()})

class EmployeesListView(APIView):
    '''Вывод списка работников'''
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeesDetailSerializer(employees, many=True)
        return Response(serializer.data)

class EmployeesDetailView(APIView):
    '''Вывод работника'''
    def get(self, request, pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeesDetailSerializer(employee)
        return Response(serializer.data)