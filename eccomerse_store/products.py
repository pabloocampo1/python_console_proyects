import random

products={}

def create_product():
    name_prodcut=input("name product: ").title()
    description=input("description: ")
    price=float(input("price: "))
    count=int(input("count: "))
    code_product=random.randint(10000,99999)
    
    
    if not code_product in products:
        products[code_product] = {
            "name product": name_prodcut,
            "description":description,
            "price": price,
            "count": count,
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
            4. add count 
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
            new_count=int(input("new count: "))
            products[code]["name"] += new_count
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
        print("no there are products")
    else:
        for i, j in products.items():
            print("         ______________")
            print(f"""
                code product {i}
                name: {j['name product']}
                
                """)
