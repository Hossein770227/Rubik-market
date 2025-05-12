from django.shortcuts import get_object_or_404, redirect, render

from cart.forms import AddToCartForm
from shop.models import Phone

from .cart import Cart

def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartForm(
            initial={'quantity':item['quantity'], 'inplace':True}
        )
    return render(request, 'cart/cart_detail.html',{'cart':cart})


def phone_add_to_cart_view(request, product_id):
    cart = Cart(request)
    
    product = get_object_or_404(Phone,pk = product_id )
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product,quantity, replace_current_quantity=cleaned_data['inplace'] )
        return redirect('cart:cart_detail')