from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Employee(MPTTModel):
    full_name = models.CharField(max_length=80, verbose_name='ФИО', blank=False)
    position = models.CharField(max_length=80, verbose_name='Должность', blank=False)
    employment_date = models.DateField(verbose_name='Дата приема', blank=False)
    salary = models.IntegerField(verbose_name='Зарплата', blank=False)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='employye')

    class MPTTMeta:
        order_insertion_by = ['full_name']

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name

