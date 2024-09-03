import django_tables2 as tables
from .models import Vendor


class VendorTable(tables.Table):
    action_button = tables.TemplateColumn(template_name='django_tables2/action_button.html', orderable=False)

    class Meta:
        model = Vendor
        fields = ("name", "contact_details", "address", "vendor_code", "on_time_delivery_rate", "quality_rating_avg", "average_response_time", "fulfillment_rate", 'action_button')
