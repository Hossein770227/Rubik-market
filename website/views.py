from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def about_view(request):
    return render(request, 'website/about.html')

@login_required
def contact_view(request):
    return render(request, 'website/contact.html')
