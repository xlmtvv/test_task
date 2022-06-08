from django.contrib import admin
from django.contrib.admin import FieldListFilter
from mptt.admin import MPTTModelAdmin
from .models import Employee
from mptt.admin import TreeRelatedFieldListFilter

@admin.register(Employee)
class CatalogAdmin(MPTTModelAdmin):
    model = Employee
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )
    mptt_level_indent = 15



