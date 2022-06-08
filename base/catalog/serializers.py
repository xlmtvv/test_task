from rest_framework import serializers
from .models import Employee

class EmployeesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('full_name', 'position', 'employment_date', 'salary', 'parent')

class EmployeesDetailSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field="full_name", read_only=True)

    class Meta:
        model = Employee
        fields = ('full_name', 'position', 'employment_date', 'salary', 'parent')


