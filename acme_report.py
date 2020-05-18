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

def inventory_report(products = generate_products()):
    '''takes a list of products, and prints a "nice" summary'''

    for i in range(len(products)):
        print("--- Product #" + str(i+1) + " ---")
        print("Name:", products[i].name)
        print("Price:", products[i].price)
        print("Weight:", products[i].weight)
        print("Flammability:", products[i].flammability)
        print("\n")

if __name__ == '__main__':
    inventory_report(generate_products())