from pyscript import display

#Variables

# String
restaurant_name = "Carrella's Cafe"
owner_name = "Leona Abeleda"

# Integer
year_established = 2025

# Floating-point
popular_item_price = 149.99
tax_rate = 0.12

# Boolean
has_delivery = False

# List
product_names = ["Matcha Latte", "Glazed Donut", "Spanish Latte"]

# Tuple
business_hours = ("11:00 AM", "9:00 PM")

# Set
common_allergens = {"Gluten", "Dairy", "Eggs"}

# Dictionary
menu_prices = {
    "Matcha Latte": 119.99,
    "Glazed Donut": 39.00,
    "Spanish Latte": 149.00,
    "Iced Tea": 79.00,
    "Sparkling Water": 60.00
}

# === for output ===
display(f"Restaurant: {restaurant_name}", target="output")
display(f"Year Established: {year_established}", target="output")
display(f"Popular Item Price: ₱{popular_item_price}", target="output")
display(f"Business Hours: {business_hours[0]} - {business_hours[1]}", target="output")
display(f"Has Delivery: {'Yes' if has_delivery else 'No'}", target="output")

# Menu
display("Menu:", target="output")
for item, price in menu_prices.items():
    display(f" - {item}: ₱{price}", target="output")

# Allergies n Tax
display(f"Common Allergens: {', '.join(common_allergens)}", target="output")
display(f"Tax Rate: {tax_rate * 100}%", target="output")
