from ClassMGL import FoodOrder

def create_list():
    num_items = int(input("How many items to order? "))
    while num_items < 1:
        num_items = int(input("Number of items must be at least 1: "))

    item_list = []

    for _ in range(num_items):
        food = input("Enter food: ")
        amount = int(input("Enter amount of selected food : "))
        while amount <= 0:
            amount = float(input("Number of pounds must be greater than 0: "))
        
        my_food = FoodOrder(food, amount)
        item_list.append(my_food)

    return item_list

def display_contents(item_list):
    for item in item_list:
        print(f"Food: {item.get_food()}, Amount: {item.get_amount_in_pounds()}, Standard Price per Pound: ${item.get_standard_price():.2f}, Calculated Price: ${item.get_calc_price():.2f}")

def calculate_total_cost(item_list):
    total_cost = sum(item.get_calc_price() for item in item_list)
    return total_cost

def main():
    items = create_list()
    display_contents(items)
    
    total_cost = calculate_total_cost(items)
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
