class FoodOrder:
    standard_prices = {
        "Dry Cured Iberian Ham": 177.80,
        'Wagyu Steaks': 450.00,
        'Matsutake Mushrooms': 272.00,
        'Kopi Luwak Coffee': 306.50,
        'Moose Cheese': 487.20,
        'White Truffles': 3600.00,
        'Blue Fin Tuna': 3603.00,
        'Le Bonnotte Potatoes': 270.81
    }

    def __init__(self, food, amount):
        self.food_name = None
        self.order_amount = None
        self.standard_price = 0
        self.calc_price = 0
        self.init_order(food, amount)

    def init_order(self, food, amount):
        self.food_name = food
        self.order_amount = amount
        self.standard_price = self.get_standard_price()
        self.calc_price = self._calculate_price()

    def get_food(self):
        return self.food_name

    def get_standard_price(self):
        return self.standard_prices.get(self.food_name, 0)

    def _calculate_price(self):
        return self.order_amount * self.standard_price

    def get_amount_in_pounds(self):
        return self.order_amount

    def get_calc_price(self):
        return self.calc_price
