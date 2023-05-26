# Azubi Store Sales Review

products = ["Sankofa Foods","Jamestown Coffee","Bioko Chocolate","Blue Skies Ice Cream","Fair Afric Chocolate","Kawa Moka Coffee","Aphro Spirit","Mensado Bissap","Voltic"]
prices = [30,25,40,20,20,35,45,50,35]
last_week = [2,3,5,8,4,4,6,2,9]

# Calculate the total price average for all products
total_products = len(products)
total_prices = sum(prices)
total_price_average = total_prices/total_products
print("Total Price Average",total_price_average)

# create a new price list that reduces the old price by 5
new_price_list = []
def reduce_price_list(amount_to_reduce):
    for product in prices:
        new_price = product + amount_to_reduce
        new_price_list.append(new_price)

reduce_price_list(5)
print("New Price list ",new_price_list)

# calcalute the total  revenue generated from the products
revenue_from_products = []
for index in range(len(prices)):
    revenue_from_products.append(prices[index] * last_week[index])

total_revenue_from_products = sum(revenue_from_products)
print("Total Revenue from products =",total_revenue_from_products)


# calculate average daily revenue generated from the products
number_of_days_in_a_week = 7
average_daily_revenue = total_revenue_from_products/number_of_days_in_a_week
print("Average daily revenue from products = ",average_daily_revenue)

# which products are less than $30 based on new prices
products_with_prices_less_than_30 = []

for index in range(len(products)):
      if new_price_list[index] < 30:
           products_with_prices_less_than_30.append(products[index])
      else:
           continue
print("Products with prices less than $30 are = ",products_with_prices_less_than_30)


