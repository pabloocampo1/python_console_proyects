import random

products = {
    23232: {
        "name product": "Apple iPhone 13",
        "description": "Smartphone with 6.1-inch display, 128GB storage",
        "price": 799,
        "quantity": 4,
        "code product": 23232,
    },
    2332: {
        "name product": "Samsung Galaxy S21",
        "description": "Android phone with 6.2-inch display, 128GB storage",
        "price": 699,
        "quantity": 4,
        "code product": 2332,
    },
    2323: {
        "name product": "Sony WH-1000XM4",
        "description": "Wireless noise-canceling headphones",
        "price": 348,
        "quantity": 4,
        "code product": 2323,
    },
    3232: {
        "name product": "Dell XPS 13",
        "description": "Laptop with 13.3-inch display, 8GB RAM, 256GB SSD",
        "price": 999,
        "quantity": 4,
        "code product": 3232,
    },
    4545: {
        "name product": "Nintendo Switch",
        "description": "Hybrid gaming console with Neon Blue and Red Joy‑Con",
        "price": 299,
        "quantity": 4,
        "code product": 4545,
    },
    5656: {
        "name product": "Amazon Echo Dot",
        "description": "Smart speaker with Alexa, 4th Gen",
        "price": 49,
        "quantity": 4,
        "code product": 5656,
    },
    6767: {
        "name product": "Apple MacBook Air",
        "description": "Laptop with 13-inch display, M1 chip, 256GB SSD",
        "price": 999,
        "quantity": 4,
        "code product": 6767,
    },
    7878: {
        "name product": "Bose QuietComfort 35 II",
        "description": "Wireless Bluetooth Headphones, Noise-Cancelling",
        "price": 299,
        "quantity": 4,
        "code product": 7878,
    },
    8989: {
        "name product": "GoPro HERO9",
        "description": "Action camera with 5K video, 20MP photos",
        "price": 399,
        "quantity": 4,
        "code product": 8989,
    },
    9090: {
        "name product": "Fitbit Charge 4",
        "description": "Fitness and Activity Tracker with GPS",
        "price": 149,
        "quantity": 4,
        "code product": 9090,
    },
}

def create_product():
    name_prodcut=input("name product: ").title()
    description=input("description: ")
    price=float(input("price: "))
    quantity=int(input("quantity: "))
    code_product=random.randint(10000,99999)
    
    if not code_product in products:
        products[code_product] = {
            "name product": name_prodcut,
            "description":description,
            "price": price,
            "quantity": quantity,
            "code product": code_product
        }
    else:
        print("the product already exist")

    
def edit_product():
    code=int(input("code product: "))
    if code in products:
        print("""
            what do you want edit?: 
            1. name
            2. description
            3. price
            4. add quantity 
        """)
        option=int(input("insert your option: "))
        if option == 1:
            new_name=input("new name: ")
            products[code]["name product"] = new_name
        elif option == 2:
            new_description=input("new description: ")
            products[code]["description"] = new_description
        elif option == 3:
            new_price=float(input("new price: "))
            products[code]["price"] = new_price
        elif option == 4:
            new_quantity=int(input("new quantity: "))
            products[code]["name"] += new_quantity
        else:
            print("option invalid")
    else:
        print("invalid code product")


def delete_product():
    id_code=int(input("code producto: "))
    if id_code in products:
        question=input(f"sure that do you want delete {products[id_code]['name']}(yes/no): ").lower()
        if question == "yes":
            del products[id_code]
            print("succesfully delete")
        elif question == "no":
            print("okey...")
          
def show_all():
    if len(products) <= 0:
        return print("no there are products")
    else:
        for i, j in products.items():
            print(f"""      ____________
                code product {i}
                name: {j['name product']}
                quantity : {j['quantity']}
                price : {j['price']}
                """)
            
            
def show_all_count():
    keys=list(products.keys())
    if len(products) <= 0:
        return print("no there are products")
    else:
        total_products=len(products)
        how_many=int(input(f"how many produts you do want to see? (total={total_products}): "))
        for i in range(how_many):
            key=keys[i]
            product=products[key]
            print("_________________")
            for k,v in product.items():
                print(f" {k} : {v}")
            
