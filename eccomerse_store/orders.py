from products import products
import random

#variables

orders_user={}
total_ordes={}
sales={}




def total_sales():
    if len(sales) >= 1:
        print("________HISTORY SALES_______")
        for i, j in sales.items():
            print("_____________________")
            print(f"invoise number {i} total products {j["quantity"]} total money {j["total money"]}")
        
        total_gains=0
        for i in sales.values():
            total_gains += i["total money"]
            
        print(f"----gains total: {total_gains}----")
    else:
        print("no there are sales.")
def shooping_card(user):
    while True:
        id_order=random.randint(10000, 99999)
        code_product=int(input("insert the code product: "))
        if code_product in products:
            option_quantity_product=int(input("how many quantity"))
            quantity_product=products[code_product]["quantity"]
            if quantity_product <=0:
                print("no there are quantify product")
            elif option_quantity_product < quantity_product:
                products[code_product]["quantity"] -= option_quantity_product
                orders_user[id_order] = {
                    "name product": products[code_product]["name product"],
                    "price product": products[code_product]["price"],
                    "quantity product": option_quantity_product,
                    "user": user["name"]
                }
            else:
                print(f"quantity invalid, only there {quantity_product}")
                
            again=input("Do you want to add more?:(yes/no) ")
            if again == "yes":
                pass
            elif again == "no":
                if len(orders_user) >= 1:
                    pay=input("do you want pay now?(yes/no): ")
                    if pay == "yes":
                        order=random.randint(10000,99999)
                        total_ordes[order] = orders_user
                        pay_account()
                else:
                    print("you have add products to shoopingcard.")
                break   
            
        else:
            print("product no found")
        
def invoise():
    id_sale=random.randint(10000, 99999)
    total_products=0
    total_price=0
    
    print("____factura____")
    for  i,j in orders_user.items():
        total_price += j["price product"] * j["quantity product"]
        total_products+=1
        print(f"""
            _________________________________________
            name product - {j['name product']}
            quantity product - {j['quantity product']}
            price  -  {j['price product']}
            code product - {i}
            """)
    print(f"el total a pagar es :  {total_price}")
    
    sales[id_sale]= {
        "id sale": id_sale,
        "quantity": total_products,
        "total money": total_price,
    }
        

def pay_account():
    global orders_user
    if len(orders_user) >= 1:
        invoise()
        count_bank=input("your count bank: ")
        password_bank=input("your password: ")
        orders_user = {}
        print("pay successfully.")
    else:
        print("you no have orders.")

    
        
        
    
