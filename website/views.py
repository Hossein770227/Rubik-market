from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from website.forms import ContactForm


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

            return redirect('shop:product-list') 
        else:
            return render(request, 'website/contact.html', {'form': contact_form}) 
    else:
        contact_form = ContactForm()
    return render(request, 'website/contact.html', {'form': contact_form}) 



