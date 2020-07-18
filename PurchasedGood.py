class PurchasedGood:
    def __init__(self, price, category = "General", tax = 0.07):
        self.price = price
        self.category = category
    self.tax = tax

    def calculate_total(self):
        total = round(self.price+(self.price*self.tax), 2)
        return total


good_1 = PurchasedGood(5.00)
print(good_1.price)
print(good_1.category)
print(good_1.tax)
print(good_1.calculate_total())

good_2 = PurchasedGood(5.00, category = "Grocery", tax = 0.03)
print(good_2.price)
print(good_2.category)
print(good_2.tax)
print(good_2.calculate_total())
