from django.urls import path
from django.views.generic import TemplateView

from fatmug_assignment.views import VendorCreateView, VendorDetailView, VendorUpdateView, VendorDeleteView, VendorListView

app_name ='fatmug_assignment'


# sample just to check my setup configured for app properly
urlpatterns = [
    path('', TemplateView.as_view(template_name='fatmug_assignment/index.html'), name='index'),
]



urlpatterns += [
    path('vendor/', VendorListView.as_view(), name='vendor_list'),
    path('vendor/create/', VendorCreateView.as_view(), name='vendor_create'),
    path('vendor/<int:pk>/', VendorDetailView.as_view(), name='vendor_detail'),
    path('vendor/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor_update'),
    path('vendor/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor_delete'),
]
