# We define the function
def get_price_with_vat(price):
    return price + price*20/100

price_without_vat = 100
# we call the function passing parameters
price_with_vat = get_price_with_vat(price_without_vat)

print(f"Price with vat: {price_with_vat}")

user_price = int(input("Enter the price without VAT:\n"))
# we call the function passing parameters
user_price_with_vat  = get_price_with_vat(user_price)

print(f"Price with vat: {user_price_with_vat}")