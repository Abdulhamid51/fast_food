from django.contrib import admin
from .models import *

admin.site.register(Category)

@admin.register(Food)
class Food(admin.ModelAdmin):
    list_display = ['name','price']
    list_display_links = ['name','price']