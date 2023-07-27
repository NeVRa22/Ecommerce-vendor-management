class Products:
    def __init__(self, product_name, product_type, available_quantity, unit_price):
        self.product_name = product_name
        self.product_type = product_type
        self.available_quantity = available_quantity
        self.unit_price = unit_price
        self.products = dict()
        self.search_product = ''

    @property
    def product_name(self):
        return self.product_name

    @product_name.setter
    def product_name(self, product_name):
        self.product_name = product_name

    @property
    def product_type(self):
        return self.product_type

    @product_type.setter
    def product_type(self, product_type):
        self.product_name = product_type

    @property
    def available_quantity(self):
        return self.available_quantity

    @available_quantity.setter
    def available_quantity(self, available_quantity):
        self.available_quantity = available_quantity

    @property
    def unit_price(self):
        return self.unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        self.unit_price = unit_price

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        self.products[product_name] = {"product_name": product_name,
                                       "product_type": product_type,
                                       "available_quantity": available_quantity,
                                       "unit_price": unit_price
                                       }

    def search_product_by_name(self, product_name):
        self.search_product = product_name
        if product_name in self.products.values():
            return True
        else:
            print('product not found')
            return False

    def get_all_products(self):
        for self.product_name in self.products.values():
            return self.product_name
