from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import OrderForm
from .tasks import prepare_order



# @login_required
# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             prepare_order.delay(order.id)
#             return redirect('order_list')
#     else:
#         form = OrderForm()
#     return render(request, 'create_order.html', {'form': form})


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'create_order.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        order = form.save()
        prepare_order.delay(order.id)
        return super().form_valid(form)


# def order_list(request):
#     orders = Order.objects.all()
#     return render(request, 'order_list.html', {'orders': orders})