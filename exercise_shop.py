products = [
    {"name": "Dell Laptop", "price": 1000},
    {"name": "Asus Laptop", "price": 1300},
    {"name": "Mac Laptop", "price": 1800},
    {"name": "Razer Laptop", "price": 2300},
]

careers = [
    {"name": "National post", "fees":20},
    {"name": "DHL Express", "fees":45},
]

# we do a for loop to display the products
for index, product in enumerate(products):
    print(f"For {product["name"]} - ${product["price"]} press {index}")

# use a input to get user choice
while True:
    user_product_index = input("Please enter the product number:\n")
    try:
        user_product_index = int(user_product_index)
        # we need to check if the number is greater or equal than 0 and less than number of products 
        if user_product_index >= 0 and user_product_index < len(products):
            break
        else:
            print("This product does not exist")
    except ValueError:
        print("Please enter only number")

user_product = products[user_product_index]


# we do a for loop to display the careers
for index, career in enumerate(careers):
    print(f"For {career["name"]}  - ${career["fees"]}  press {index}")

# use a input to get user choice
while True:
    user_career_index = input("Please enter the career number:\n")
    try:
        user_career_index = int(user_career_index)
        # we need to check if the number is greater or equal than 0 and less than number of careers 
        if user_career_index >= 0 and user_career_index < len(careers):
            break
        else:
            print("This career does not exist")
    except ValueError:
        print("Please enter only number")

user_career = careers[user_career_index]

print(f"You choose {user_product["name"]} - ${user_product["price"]}")
print(f"Career: {user_career["name"]} - ${user_career["fees"]}")

total = user_product["price"] + user_career["fees"]

print(f"Total to pay ${total}")
