from django.contrib import admin
from ras.models import ComplektSK, ComplektSKCalc


class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'weight')
    search_fields = ('name',)

admin.site.register(ComplektSK, NameAdmin)
admin.site.register(ComplektSKCalc, NameAdmin)
