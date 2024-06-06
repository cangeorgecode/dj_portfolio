from django.contrib import admin
from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name', 'categories', 'url', 'description']

admin.site.register(Portfolio, PortfolioAdmin)
