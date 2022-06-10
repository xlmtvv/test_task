from rest_framework import serializers
from .models import Employee
from rest_framework_recursive.fields import RecursiveField


class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'parent','full_name', 'position', 'employment_date', 'salary', 'employee')


class EmployeesTreeSerializer(serializers.ModelSerializer):

    employee = RecursiveField(many=True, required=False)


    class Meta:
        model = Employee
        fields = ('full_name', 'position', 'employment_date', 'salary', 'employee')



