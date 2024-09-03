from django.db import models
from django_lifecycle import hook, LifecycleModelMixin
from enumfields import EnumField

from fatmug_assignment.enums import StatusType


# Create your models here.
class Vendor(LifecycleModelMixin, models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, null=True, blank=True, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0, null=True, blank=True)
    quality_rating_avg = models.FloatField(default=0.0, null=True, blank=True)
    average_response_time = models.FloatField(default=0.0, null=True, blank=True,)
    fulfillment_rate = models.FloatField(default=0.0, null=True, blank=True,)

    def __str__(self):
        return self.name

    @hook('after_create')
    def generate_vender_code(self):
        self.vendor_code = f"VC_{self.pk}"
        self.save(update_fields=['vendor_code'])


class PurchaseOrder(LifecycleModelMixin, models.Model):
    po_number = models.CharField(max_length=50, null=True, blank=True, unique=True)
    vendor = models.ForeignKey(Vendor, null=True, blank=True, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField(null=True, blank=True,)
    quantity = models.IntegerField()
    status = EnumField(enum=StatusType, default=StatusType.PENDING)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True, blank=True) # when po assigned to vender, time will add
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

    @hook('after_create')
    def generate_po_number(self):
        self.po_number = f"PON_{self.pk}"
        self.save(update_fields=['po_number'])


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date.strftime('%Y-%m-%d')}"