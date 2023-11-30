# this is my main function
# I'm gonna make a few functions that take input from the user
# and calculates the lowest car cost.

from calculator import *

print("Welcome to the car calculator. We have the following brands in our database:")
print("")
for key, value in maintenance_costs.items():
    print(key, end=", ")
print("")
gas_price = get_gas_prices()
print("These are the gas prices in your state:")
for key, value in gas_price.items():
    print(key.capitalize(), ": $", value)

months_to_75k, city_miles_month, hway_miles_month = get_user_statistics()

n = int(input("Enter the number of cars you wish to compare:"))
total_costs = {}

for i in range(n):
    car_brand = input(
        "Enter the brand of the car among the ones listed in our database: "
    ).capitalize()
    if car_brand not in maintenance_costs.keys():
        print("Car brand not recognized")
    monthly_maintenance_cost = get_monthly_maintenance_costs(months_to_75k, car_brand)
    monthly_gas_cost = get_car_mileage(city_miles_month, hway_miles_month, gas_price)
    monthly_interest_payment = get_monthly_interest_rate()
    total_cost_monthly = (
        monthly_maintenance_cost + monthly_gas_cost + monthly_interest_payment
    )
    total_costs[car_brand] = total_cost_monthly
    print(
        f"You will incur a monthly maintenance cost of: ${monthly_maintenance_cost:.2f}"
    )
    print(f"You will incur a monthly gas cost of: ${monthly_gas_cost:.2f}")
    print(
        f"You will incur a monthly interest payment of: ${monthly_interest_payment:.2f}"
    )
    print(f"Your total monthly costs for this car will be: ${total_cost_monthly:.2f}")

print("The total monthly breakdown of all cars is:")
for key, value in total_costs.items():
    print(key.capitalize(), ":$", value)
print(
    "The cheapest car based on monthly payments is the",
    min(total_costs, key=total_costs.get).capitalize(),
)
