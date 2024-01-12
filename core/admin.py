from django.contrib import admin
from .models import *
# Register your models here.
class Filter(admin.ModelAdmin):
    list_display = ('title', 'category', 'name', 'date',)
    list_filter = ('date',)
admin.site.register(Cloapedia, Filter)