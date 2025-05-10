from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

from .models import Address

@login_required
def personal_info(request):
    return render(request, 'dashboard/personal_info.html')



@login_required
def address_view(request):
    
    address = Address.objects.filter(user=request.user)
    return render(request, 'dashboard/address.html', {'address':address})
