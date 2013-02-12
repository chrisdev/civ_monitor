from django.contrib import admin
from .models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'description']
    search_fields = ('code', 'description',)

admin.site.register(Currency, CurrencyAdmin)
