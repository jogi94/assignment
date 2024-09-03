from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView

from fatmug_assignment.forms import VendorForm
from fatmug_assignment.models import Vendor
from fatmug_assignment.tables import VendorTable

# Create your views here.
class VendorListView(SingleTableView):
    model = Vendor
    table_class = VendorTable
    context_object_name = 'vendors'
    template_name = 'fatmug_assignment/vendor_list.html'


class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'fatmug_assignment/vendor_detail.html'


class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'fatmug_assignment/vendor_form.html'
    success_url = reverse_lazy('fatmug_assignment:vendor_list')


class VendorUpdateView(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'fatmug_assignment/vendor_form.html'
    success_url = reverse_lazy('fatmug_assignment:vendor_list')


class VendorDeleteView(DeleteView):
    model = Vendor
    success_url = reverse_lazy('fatmug_assignment:vendor_list')
