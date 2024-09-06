from django.urls import path, re_path
from .views import *
from django.views.generic import ListView
from .models import *

urlpatterns = [
    # re_path(r'^create/$', views.create_order, name='create_order'),
    re_path(r'^create/$', CreateOrderView.as_view(), name='create_order'),
    # re_path(r'^list/$', views.order_list, name='order_list'),
    re_path(r'^list/$', ListView.as_view(model=Order, template_name='order_list.html'), name='order_list'),
]
