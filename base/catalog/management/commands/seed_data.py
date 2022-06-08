from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from catalog.models import Employee

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):

        fake = Faker()

        for _ in range(10):
            Employee.objects.create(full_name=fake.name(), position=fake.job(), employment_date=fake.date() ,salary=randint(1000,2000), parent_id=randint(50005, 50010))

        print('Данные успешно добавлены')
