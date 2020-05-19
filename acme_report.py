import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    '''should generate a given number of products (default 30), randomly, and return them as a list'''

    products = []
    for _ in range(num_products):
        name = random.sample(ADJECTIVES, 1)[0] + " " + random.sample(NOUNS, 1)[0]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name, price, weight, flammability)
        products.append(product)

    return products

def inventory_report(products):
    '''takes a list of products, and prints a "nice" summary'''

    print("\nACME CORPORATION OFFICIAL INVENTORY REPORT")

    print("Unique product names:", len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].price
    print("Average price:", total / len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].weight
    print("Average weight:", total / len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].flammability
    print("Average flammability:", total / len(products))

if __name__ == '__main__':
    inventory_report(generate_products())