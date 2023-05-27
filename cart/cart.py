from decimal import Decimal


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __len__(self):
        return len(self.cart.values())

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'name': str(product.name),
                                     'price': str(product.price),
                                     'discount': str(product.discount)+'%'}
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def list_products(self):
        return self.cart
