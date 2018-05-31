from django.contrib import admin
from .models import ATI, Department


@admin.register(ATI)
class ATIAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Details', {'fields': ['request_no', 'desc_en', 'desc_fr', 'dept']}),
        ('Date', {'fields': ['year', 'month']}),
    ]
    def ati_departments(self, obj):
        return obj.list_departments()

    list_display = ('request_no', 'ati_departments', 'year', 'month', 'desc_en', 'desc_fr')
    list_editable = ('year', 'month')
    list_display_links = ('request_no', 'ati_departments')
    list_filter = ('year', 'month')
    search_fields = ('desc_en', 'desc_fr')
    #readonly_fields = ('year', 'month',)


# Register your models here.
admin.site.register(Department)
