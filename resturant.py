def add_menu_item(menu, item):
    if item not in menu:
        menu.append(item)
def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in the menu.")
def check_item_availability(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
add_menu_item(initial_menu, add_item)
remove_menu_item(initial_menu, remove_item)
print("Updated menu:", initial_menu)
print("Availability:", check_item_availability(initial_menu, check_item))
