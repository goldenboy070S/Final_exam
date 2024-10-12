from django.contrib import admin
from .models import Daily_cost
# Register your models here.
@admin.register(Daily_cost)
class DailyCostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'amount', 'date')
    