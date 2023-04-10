




class store:
    def __init__(self):
        self.store_name = "bolt store"
        self.list_of_products = []
        self.store_price = []
    def add_product(self, new_product, s_price):
        self.list_of_products.append(new_product)
        self.store_price.append(s_price)
        return self
    def sell_product(self, id):
        print(f"{self.list_of_products[id]}, ${self.store_price[id]}")
        self.list_of_products.pop(id)
        self.store_price.pop(id)
        print(f"{self.list_of_products}")
        return self
    def inflation(self, percent_increase, id):
        self.store_price[id] = self.store_price[id] + (self.store_price[id] * percent_increase)
        print(f"${self.store_price}")
        return self
    def set_clearance(self, category, percent_discount):
        if self.store_price[category]:
            self.store_price[category] = self.store_price[category] - (self.store_price[category] * percent_discount)
        print(f"${self.store_price}")
        return self




