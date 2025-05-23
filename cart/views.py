from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect



from products.models import Product

from .cart import Cart
from .forms import AddToCartForm

def cart_detail_view(request):
    cart = Cart(request)
    
    for item in list(cart):
        item['product_update_quantity_form'] = AddToCartForm(
            initial={'quantity':item['quantity'], 'inplace':True}
        )
    return render(request, 'cart/cart_detail.html',{'cart':list(cart)})



def add_to_cart_view(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product,pk = pk )
    
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product,quantity, replace_current_quantity=cleaned_data['inplace'] )
        return redirect('cart:cart_detail')
    

def remove_form_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')

def clear_cart(request):
    cart = Cart(request)
    if cart is not None:
        cart.clear()
        return redirect('cart:cart_detail')

