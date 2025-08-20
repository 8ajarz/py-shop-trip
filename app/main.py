import json

import app.calculations as calculations
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file:
        cs_list = json.load(file)
    fuel_price = cs_list["FUEL_PRICE"]
    shops = []
    for shop in cs_list["shops"]:
        shops.append(Shop(shop))

    for customer in cs_list["customers"]:
        customer = Customer(customer)
        print(f"{customer.name} has {customer.money} dollars")
        nearest_shop = []
        for shop in shops:
            total = 0
            receipt = {}
            trip_dist = calculations.get_distance(shop, customer)
            ride = customer.fuel_consumption * fuel_price
            fuel_cost = trip_dist / 100 * ride
            total, receipt = calculations.purchases(
                total, receipt, customer, shop)
            trip_cost = round(fuel_cost * 2 + total, 2)
            # Ugly indentations - because of flake8.
            print(
                f"{customer.name}'s trip to the",
                f"{shop.name} costs {trip_cost}")
            if not nearest_shop:
                nearest_shop.append(shop)
                nearest_shop.append(trip_cost)
            else:
                if trip_cost < nearest_shop[1]:
                    nearest_shop[0] = shop
                    nearest_shop[1] = trip_cost

        if total > customer.money:
            print(
                f"{customer.name} doesn't have enough money",
                "to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {nearest_shop[0].name}\n")
            total, receipt = calculations.purchases(
                0, {}, customer, nearest_shop[0])
            print(calculations.get_receipt(receipt, customer, total))
            budget = customer.money - nearest_shop[1]
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {budget} dollars\n")


shop_trip()


if __name__ == "__main__":
    pass
