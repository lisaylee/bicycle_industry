import random

from bicycle_industry import Bike, Bike_shop, Customer

# Create a bicycle shop that has 6 different bicycle models in stock. Shop should charge 20% over cost of bikes
bike1 = Bike("Mountain", 4, 500)
bike2 = Bike("BMX",3, 100)
bike3 = Bike("Electric", 5, 1000)
bike4 = Bike("Road", 2, 700)
bike5 = Bike("Racing", 1, 800)
bike6 = Bike("Foldable", 4, 200)

peddler_bikes = Bike_shop('Peddler Bikes', 0.2)
peddler_bikes.add_bikes(bike1, 4)
peddler_bikes.add_bikes(bike2, 4)
peddler_bikes.add_bikes(bike5, 2)
peddler_bikes.add_bikes(bike6, 5)

# Add instances of bikes to a list
bikes = [bike1, bike2, bike4, bike5]

# Create 3 customer - one has budget of $200, one of $500, and of one $1000
lisa = Customer("Lisa Lizard", 200)
emily = Customer("Emily Kangaroo", 500)
angie = Customer("Angie Lionness", 1000)

# Add instances of customers to a list
customers = [lisa, emily, angie]

# Print the initial inventory of the bike shop for each bike it carries
print("Peddler Bikes carries the followig bicycles:")
print(peddler_bikes.inventory)

# Print name of each customer, and list of bikes offered by shop that they can afford
for customer in customers:
    print("******************************************************")
    print("Customer Name:" + " " + customer.name)
    print(customer.name + " " + "can afford to buy the following bikes:")
    print(customer.affordable(peddler_bikes))

# Have each of the customers purchase a bike then print the name of the bike the customer purchased
# The cost
# And how much money they have left over in their bicycle fund 

peddler_bikes.sell_bike(angie)
peddler_bikes.sell_bike(lisa)
peddler_bikes.sell_bike(emily)

print("******************************************************")
for customer in customers:
    print (customer.name, 'bought:', customer.purchases, 'Budget remaining:', '{:.2f}'.format(customer.budget))


# After customer has purchased bike, print the bicycle's remaining inventory and profit
print("******************************************************")
peddler_bikes.print_stock()
print('Peddler Bikes', 'profit:', '{:.2f}'.format(peddler_bikes.profit))