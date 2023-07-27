from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):

    def __init__(self, username, product_name, product_type, available_quantity, unit_price):
        super().__init__(product_name, product_type, available_quantity, unit_price)
        self.product_model = ProductModel
        self.vendor_session = VendorSessionModel
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        if self._username in VendorSessionModel.vendor_session_db[self._username]
            return True
        self.products[product_name] = {"product_name": product_name,
                                       "product_type": product_type,
                                       "available_quantity": available_quantity,
                                       "unit_price": unit_price
                                       }


        # check if the vendor is logged in, then add the product and return True else Return False
            
    def search_product_by_name(self, product_name):
        self.search_product = product_name
        if product_name in self.products.values():
            return True
        else:
            return None
        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product

    def get_all_products(self):
        for self.product_name in self.products.values():
            return self.product_name
        else:
            return False
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products 

