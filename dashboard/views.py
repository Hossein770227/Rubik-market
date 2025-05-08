from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def personal_info(request):
    return render(request, 'dashboard/personal_info.html')