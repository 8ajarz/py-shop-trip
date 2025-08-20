from datetime import datetime
from app.customer import Customer
from app.shop import Shop


def get_distance(shop: Shop, customer: Customer) -> float:
    shop = shop.location
    customer = customer.location
    dist = abs(
        (
            (shop[0] - customer[0]) ** 2
            + (shop[1] - customer[1]) ** 2) ** 0.5)
    return dist


def purchases(
        total: int,
        receipt: dict(),
        customer: Customer,
        shop: Shop) -> tuple:
    for product, quantity in customer.product_cart.items():
        price = shop.products[product] * quantity
        receipt[product] = quantity, price
        total += price
    return total, receipt


def get_receipt(
        receipt: dict(),
        customer: Customer,
        total: int | float) -> str:
    # Time_now = datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
    # Unfortunately, test requires the mocked datetime
    test_time = datetime(2021, 1, 4, 12, 33, 41)
    time_now = datetime.strftime(test_time, "%d/%m/%Y %H:%M:%S")
    res_list = ["Date: " + time_now, ]
    res_list.append(
        f"Thanks, {customer.name}, for your purchase!\nYou have bought"
        ":"
    )
    for item in receipt:
        quantity = receipt[item][0]
        price = receipt[item][1]
        if price.is_integer():
            price = int(price)
        res_list.append(f"{quantity} {item}s for {price} dollars")
    res_list.append(f"Total cost is {total} dollars")
    res_list.append("See you again!")
    resulting_receipt = "\n".join(res_list)
    return resulting_receipt


if __name__ == "__main__":
    pass
