from django.urls import path
from django.views.generic import TemplateView

app_name ='fatmug_assignment'

urlpatterns = [
    path('', TemplateView.as_view(template_name='fatmug_assignment/index.html'), name='index'),
]
