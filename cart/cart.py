
from products.models import Product


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product , quantity=1, replace_current_quantity=False):
        product_id = str(product.id)
        if not product_id in self.cart:
            self.cart[product_id]={'quantity':0}

        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()
    
    def save(self):
        self.session.modified = True
    
    def remove(self, product):
       product_id = str(product.id)
       if product_id in self.cart:
           del self.cart[product_id]
           self.save()
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product
        
        for item in cart.values():
            item['total_price'] = item['product_obj'].price_without_discount * item['quantity']
            yield item

    def __len__(self):
        result = 0
        for i in self.cart.values():
            result += i
        return result

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.values()
        return (sum(item['quantity'] * item['product_obj'].price_without_discount for item in self.cart.values()))