# Cart Management system
class Cart:
    def __init__(self, item):
        self.item = item
        self.prices = []
        self.cart = []
        self.total = 0
    
# Kijani groceries cart will enable our customers to add their 
# selected items to be added to the cart to make it easier to know what to pay for
    
    def add_to_cart(self,items):
        while True:
            item = input("Select an item (q to quit):")
            if item == "q":
                break
            else:
                self.cart.append(item)
                price = input(f"Enter the price of {item}")
                self.prices.append(price)
            for item in self.cart:
                print(item)
            for price in self.prices:
                total += price
                print(f"Your total amount is:ksh{total}")






            






    
