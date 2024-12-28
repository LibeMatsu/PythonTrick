def apply_discount(product, discount):
    price = int(product['price'] * (1.0 -discount))
    assert 0 <= price <= product['price']
    return price


# product = {'price': 100}
# ↓ 10%off ↓
# discount = 0.10 
# print(apply_discount(product, discount))


# product = {'price': 100}
# ↓ 1000%off ※AssertionErrorを発生させる※ ↓
# discount = 10
# print(apply_discount(product, discount))


shoes = {'name': 'Fancy Shoes', 'price': 14900}

# print(apply_discount(shoes, 0.25))

# print(apply_discount(shoes, 2.0))


# assert_stmt ::= "assert" expression1 ["," expression2]
# assert x > 0, "x must be positive"

def apply_discount2(product, discount):
    price = int(product['price'] * (1.0 -discount))
    assert 0 <= price <= product['price'] , "priceの値は0以上、商品価格以下になるように設定しなくてはいけません"
    return price

print(apply_discount2(shoes, 2.0))


# assert (tuple, 'A non-empty tuple is always TRUE')
# 空でないタプルは常にTrueになるのでassertionがFalseにならないよ

