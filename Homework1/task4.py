#func to calc discount price
def calculate_discount(price, discount):
    discount = discount / 100
    disc_price = round(price - (price * discount), 2)
    return disc_price

#pytest with different values
def test_calc_discount():
    assert calculate_discount(50, 10) == 45.0
    assert calculate_discount(75.50, 20.5) == 60.02
    assert calculate_discount(100, 0) == 100.0
    assert calculate_discount(150, 99.99) == 0.02