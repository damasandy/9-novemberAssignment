inventory_quantity=int(input("enter inventory quantity"))
try:
    user_quantity=int(input("Enter the quantity you want to purchase:"))
    if user_quantity<=0:
        raise ValueError("Quantity should be a positive number")
    if user_quantity > inventory_quantity:
        raise ValueError(f"sorry,we have only{inventory_quantity}items in stock.")
    quantity_increase = user_quantity - inventory_quantity
    inventory_quantity = user_quantity
    print(f"product added to the flipkartcard.quantity increased by {quantity_increase}.")
except ValueError as e:
    print(f"Error:{e}")
except ZeroDivisionError:
    print("ZeroDivisionError occured.")
except Exception as e:
    print(f"An unexpected erroroccured:{e}")