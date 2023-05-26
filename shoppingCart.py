
shoping_cart = []
item_prices = []
product_and_price = {}
# menu items
app_menu = {
    1: "Add Item",
    2: "Remove Item",
    3: "View content of shopping cart",
    4: "Calculate Shopping Cart",
    5: "End"
}

#  function for option 1
def option_1():
    item_name = input("What is the name of the item you want to add: ")
    item_price = input("What is price of the item: ")
    product_and_price={item_name:item_price}
    shoping_cart.append(product_and_price)
    print("Item added")
    print("\n")

#  function for option 2
def option_2():
    item = str(input("What is the name of the item to remove: "))
    item_to_remove_index = find_item_in_list(shoping_cart,item)
    if item_to_remove_index != "none":
      shoping_cart.pop(item_to_remove_index)
      print("Item removed")
      print("\n")
    else:
      print("Item does not exist")
      print("\n")
    
#  function for option 3
def option_3():
    if len(shoping_cart) == 0:
       print("You have no items in shopping cart")
       print("\n")
    else:
     for item in shoping_cart:
        print_items(item)
     print("\n")

#  function for option 4
def option_4():
    for item in shoping_cart:
        for x in item:
            item_prices.append(int(item[x]))
    print(f'Sum of item in shiopping cart: {sum(item_prices)} ')
    print("\n")

#  function for printing munu items
def print_menu():
    for key in app_menu.keys():
        print (key, '--', app_menu[key] )

#find item in a list
def find_item_in_list(lst, key):
    for i, dic in enumerate(lst):
        if dic[key]:
            return i
    return "none"

#print list items
def print_items(item):
   for x,y in item.items():
    print(f'Item name: {x},',f'Item price: {y}')


print("Welcome to shoping cart application")
program_on = True
while program_on:
    try:
        print_menu()
        option = int(input("Enter your choice: "))
        if option == 1:
         option_1()
        elif option == 2:   
         option_2()
        elif option == 3:
         option_3()
        elif option == 4:
         option_4()
        elif option == 5:
         print("Good Bye!!!!")
         program_on = False
        else:
         print("Please enter a number between 1-5") 
    except ValueError:
        print("Please enter a number between 1-5")
        continue
    

        



