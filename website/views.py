from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.http import require_GET, require_POST

from .forms import ContactForm

from shop.models import Phone


def about_view(request):
    
    return render(request, 'website/about.html')


@login_required()
def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_message = contact_form.save(commit=False)
            contact_message.user = request.user
            contact_message.save() 

            return redirect('shop:product_ist') 
        else:
            return render(request, 'website/contact.html', {'form': contact_form}) 
    else:
        contact_form = ContactForm()
    return render(request, 'website/contact.html', {'form': contact_form}) 


def question_view(request):
     return render(request, 'website/question.html')



@require_GET
def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Phone.objects.filter(
            Q(title__icontains=query) | Q(brand__name__icontains=query)
        )
       

    return render(request, 'website/search_results.html', {'results': results, 'query': query})


