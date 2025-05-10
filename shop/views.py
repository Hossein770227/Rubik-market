from django.shortcuts import render, get_object_or_404
from django.views import generic

from shop.forms import CommentPhoneForm
from shop.models import CommentPhone, Laptop, Phone

class ProductList(generic.TemplateView):
    template_name = 'shop/product_list.html'


class PhoneListView(generic.ListView):
    model = Phone
    template_name = 'shop/phone_list.html'
    context_object_name = 'phones'

    def get_queryset(self):
        return Phone.objects.filter(is_active=True)


class PhoneDetailView(generic.DetailView):
    model = Phone
    template_name = 'shop/phone_detail.html'
    context_object_name = 'phone'


def comment_phone_view(request, pk):
    product = get_object_or_404(Phone, pk=pk)
    comments = CommentPhone.objects.filter(active=True)
    if request.method =='POST':
        comment_form =CommentPhoneForm(request.POST)
        if comment_form.is_valid():
           new_comment = comment_form.save(commit=False)
           new_comment.author = request.user
           new_comment.save()
           comment_form = CommentPhoneForm()
    else:
        comment_form = CommentPhoneForm()
    return render (request,'shop/phone_detail.html', {'comments':comments, 'form':comment_form})



class LaptopListView(generic.ListView):
    model = Laptop
    template_name = 'shop/laptop_list.html'
    context_object_name = 'laptops'

    def get_queryset(self):
        return Laptop.objects.filter(is_active=True)
    


class LaptopDetailView(generic.DetailView):
    model = Laptop
    template_name = 'shop/laptop_detail.html'
    context_object_name = 'laptop'