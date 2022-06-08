from django.urls import path
from .views import *

urlpatterns = [
    path('employees/', EmployeesListView.as_view()),
    path("employees/<int:pk>/", EmployeesDetailView.as_view())
]