from django.contrib import admin
from .models import PurchaseOrder, Vendor, HistoricalPerformance


# Register your models here.


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    # list_display = ('po_number',)  # display the po_number field in the admin list view
    pass


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    # list_display = ('po_number',)  # display the po_number field in the admin list view
    pass


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    pass