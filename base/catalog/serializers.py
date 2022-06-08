from rest_framework import serializers
from .models import Employee

class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data

class EmployeesListSerializer(serializers.ModelSerializer):

    employye = RecursiveSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('full_name', 'position', 'employment_date', 'salary', 'employye')





class EmployeesDetailSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field="full_name", read_only=True)

    class Meta:
        model = Employee
        fields = ('full_name', 'position', 'employment_date', 'salary', 'parent')
