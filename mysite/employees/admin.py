from django.contrib import admin
from .models import *


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'surname', 'male_or_female', 'age')


class CatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Category, CatsAdmin)
admin.site.register(Position, PosAdmin)
# admin.site.register(Gender)

# Register your models here.
