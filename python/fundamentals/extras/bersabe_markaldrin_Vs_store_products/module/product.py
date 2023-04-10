class product:
    
    def __init__(self, p_name, p_price, p_category):
        self.product_name = p_name
        self.price = p_price
        self.category = p_category
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + (self.price * percent_change)
        else:
            if is_increased == False:
                self.price = self.price - (self.price * percent_change)
        print(self.price)
        return self
    def print_info(self):
        print(f"{self.product_name} => {self.category} => ${self.price}")
        return self

    
