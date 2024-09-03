from django.contrib import admin
from .models import PurchaseOrder, Vendor, HistoricalPerformance


# Register your models here.


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    readonly_fields = ('vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time',
                       'fulfillment_rate')
    list_display = ('vendor_code', 'name', 'contact_details', 'address')
    fields = (
        'name',
        'contact_details',
        'address',
        'vendor_code',
        'on_time_delivery_rate',
        'quality_rating_avg',
        'average_response_time',
        'fulfillment_rate',
    )


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('po_number',)
    list_display = ('po_number', 'vendor', 'status')
    fields = (
        'po_number',
        'vendor',
        'status',
        'order_date',
        'delivery_date',
        'items',
        'quantity',
        'quality_rating',
        'issue_date',
        'acknowledgment_date',
    )