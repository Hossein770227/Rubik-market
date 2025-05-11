from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView



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

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['addresses'] = Address.objects.filter(user=self.request.user)
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        messages.success(self.request, 'Address saved successfully!') 
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'please inter your information correctly.') 
        return self.render_to_response(self.get_context_data(form=form))


class UpdateAddressView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'dashboard/update_address.html'
    success_url = reverse_lazy('dashboard:address') 

    def test_func(self):
        return self.request.user == self.get_object().user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.filter(user=self.request.user)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Address updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error updating the address. Please correct the errors below.')
        return super().form_invalid(form)


class DeleteAddressView(DeleteView):
    model = Address
    template_name = 'dashboard/delete_address.html'
    success_url = reverse_lazy('dashboard:address')

    def form_valid(self, form):
        messages.error(self.request, 'Address delete successfully!')
        return super().form_valid(form)