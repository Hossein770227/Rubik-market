from shop.models import Laptop, Phone

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, product_type, quantity=1, replace_current_quantity=False):
        product_id = str(product.id)
        if not product_id in self.cart:
            self.cart[product_id] = {'quantity': 0, 'type': product_type}

        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session['cart']
        self.save()


    def __iter__(self):
        product_ids = self.cart.keys()
        try:
            products = Phone.objects.filter(id__in=product_ids)
        except:
            products = Laptop.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product
        
        for item in cart.values():
            item['total_price'] = item['product_obj'].price_without_discount * item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    

    def get_total_price(self):
        total = 0
        for item in self.cart.values():
            if 'product_obj' in item:  
                total += item['quantity'] * item['product_obj'].price_without_discount
        return total
    
    # def total_discount(self):
    #     product_ids = self.cart.keys()
    #     return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())







