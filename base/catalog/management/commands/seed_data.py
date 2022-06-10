from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from catalog.models import Employee


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):

        fake = Faker()

        Employee.objects.create(full_name='Steve Jobs', position='CEO', employment_date=fake.date(),
                                salary=randint(1000, 2000))
        p_id = 1
        for _ in range(4):

            Employee.objects.create(full_name=fake.name(), position=fake.job(), employment_date=fake.date() ,salary=randint(1000,2000), parent_id=p_id)
            p_id += 1

        for _ in range(49995):
            Employee.objects.create(full_name=fake.name(), position=fake.job(), employment_date=fake.date() ,salary=randint(1000,2000), parent_id=randint(1,5))

        print('Данные успешно добавлены')
