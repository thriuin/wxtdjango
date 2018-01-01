from django.contrib import admin
from .models import ATI


@admin.register(ATI)
class ATIAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ATI Details', {'fields': ['request_no', 'desc_en', 'desc_fr']}),
        ('Review', {'fields': ['year', 'month', 'orgname_en', 'orgname_fr']}),
    ]

    #readonly_fields = ('year', 'month',)
    list_display = ('request_no', 'year', 'month', 'orgname_en', 'orgname_fr', 'desc_en', 'desc_fr')
    list_editable = ('desc_en', 'desc_fr')
    list_display_links = ('request_no', 'year', 'month')
    list_filter = ('year', 'month', 'orgname_en')
    search_fields = ('orgname_en', 'desc_en')

# Register your models here.
# admin.site.register(ATI)