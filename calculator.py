# This is the main file for all the calculations.
from scraper import *
from car_maintenance_costs import maintenance_costs

url = "https://gasprices.aaa.com/state-gas-price-averages/"
gas_price = scrape_for_gas_prices(url)


def get_gas_prices():
    user_state = input("Please enter your State:").capitalize()
    if user_state in gas_price:
        state_prices = gas_price[user_state]
    return state_prices


def get_user_statistics():
    city_weekday_miles = float(
        input("How many miles do you travel in the city on weekdays on average (M-F): ")
    )
    city_weekend_miles = float(
        input("How many miles do you travel in the city on weekends on average (S-S): ")
    )
    hway_weekday_miles = float(
        input(
            "How many miles do you travel on the highway on weekdays on average (M-F): "
        )
    )
    hway_weekend_miles = float(
        input(
            "How many miles do you travel on the highway on weekends on average (S-S): "
        )
    )
    city_miles_month = (city_weekday_miles * 5 + city_weekend_miles * 2) * 52 / 12
    hway_miles_month = (hway_weekday_miles * 5 + hway_weekend_miles * 2) * 52 / 12
    total_miles_month = city_miles_month + hway_miles_month
    months_to_75k = 75000 / total_miles_month
    return months_to_75k, city_miles_month, hway_miles_month


def get_monthly_maintenance_costs(months_to_75k, car_brand):
    return maintenance_costs[car_brand] / months_to_75k


def get_car_mileage(city_miles_month, hway_miles_month, state_prices):
    city_mileage = float(input("Please enter the city mileage of the car: "))
    hway_mileage = float(input("Please enter the highway mileage of the car: "))
    fuel_type = input(
        "Please enter the fuel type of the car(Regular/Midgrade/Premium/Diesel): "
    ).capitalize()
    if fuel_type in state_prices:
        cost_per_gallon = float(state_prices[fuel_type])
    total_gas_cost = (city_miles_month / city_mileage) * cost_per_gallon + (
        hway_miles_month / hway_mileage
    ) * cost_per_gallon
    return total_gas_cost


def get_monthly_interest_rate():
    principal = float(input("Please enter the principal amount of the loan: "))
    interest_rate = float(input("Please enter the interest rate per year: "))
    duration = float(input("Please enter the duration of the loan in years: "))
    down_payment = float(
        input("Please enter the down payment (0 if no down payment): ")
    )
    tax_rate = float(input("Please enter the sales tax rate of the purchase: "))
    amount_owed = principal + principal * tax_rate / 100
    amount_owed = amount_owed - down_payment
    monthly_interest_rate = (interest_rate / 100) / 12
    if monthly_interest_rate == 0:
        monthly_payment = amount_owed / (duration * 12)
    else:
        monthly_payment = (amount_owed * monthly_interest_rate) / (
            1 - (1 + monthly_interest_rate) ** (-duration * 12)
        )
    return monthly_payment
