from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView



from .forms import AddressForm
from .models import Address


@login_required
def personal_info(request):
    return render(request, 'dashboard/personal_info.html')


class AddressView(LoginRequiredMixin,CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'dashboard/address.html'
    success_url = reverse_lazy('dashboard:address')

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


# @login_required
# def address_view(request):
    
#     address = Address.objects.filter(user=request.user)
#     return render(request, 'dashboard/address.html', {'address':address})
