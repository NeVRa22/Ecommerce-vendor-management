class ProductModel:

    def __init__(self, product_name):
        self.product_db = dict()
        self.product_name = product_name

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        self.product_db[product_name] = {"product_name": product_name,
                                         "product_type": product_type,
                                         "available_quantity": available_quantity,
                                         "unit_price": unit_price
                                         }
        return True

    def search_product(self, product_name):
        self.product_name = product_name
        if product_name in self.product_db.values():
            return True
        else:
            print('Product not found.')
            return False

        # Search the passed product_name in the dictionary and return the value

    def all_products(self):
        if self.product_db.values is None:
            print('No products found')
        else:
            return self.product_db.values()


        # return all the products available in the dictionary
