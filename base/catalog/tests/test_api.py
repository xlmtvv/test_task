from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase

from catalog.models import Employee
from catalog.serializers import RecursiveSerializer, EmployeesSerializer


class EmployeesApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('employee-list')
        print(url)
        response = self.client.get(url)
        print(response)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
