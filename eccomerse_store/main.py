from users import create_count, users_db, change_password
from products import create_product, edit_product, show_all, delete_product, show_all_count
from orders import total_sales, shooping_card, invoise, pay_account

def menu(user):
    if user["rol"] == "user":
        while True:
            print("""
                ______MENU______
                1. show products
                2. order product
                3. show shoopingcard
                4. buy invoise
                5. log out    
             """)
            option_user=int(input("select your option: "))
            if option_user == 1:
                show_all_count()
            elif option_user == 2:
                shooping_card(user)
            elif option_user == 3:
                invoise()
            elif option_user == 4:
                pay_account()
            elif option_user == 5:
                log_in()
                
    elif user["rol"] == "admin":
        while True:
            print("""
              MENU
              ___________
              
              1. add new product
              2. edit product
              3. delete product
              4. all products
              5. show total sales
              6. change user name or password
              7. log out
            """)
            option_admin=int(input("select your option: "))
            
            if option_admin == 1:
                while True:
                    create_product()
                    again=input("Do you want add more products?(yes/no): ")
                    if again == "yes":
                        pass
                    elif again == "no":
                        break
            elif option_admin == 2:
                edit_product()
            elif option_admin == 3:
                delete_product()
            elif option_admin == 4:
                show_all()
            elif option_admin == 5:
                total_sales()
            elif option_admin == 6:
                change_password()
            elif option_admin == 7:
                log_in()
            else:
                print("option invalid")


def log_in():
    print("________welcome to log in____________")
    
    isRegistered=input("are you registered?: (yes/no)")
    if isRegistered == "yes":
        while True:
            user_name=input("write your user name: ").lower()
            if user_name in users_db:
                password=input("write your password: ")
                if password == users_db[user_name]["password"]:
                    menu(users_db[user_name])
                    break
                
            else:
                print("your user name is invalid, try again") 
    elif isRegistered == "no":
        print("You have to create an count")
        create_count()
        log_in()
        
if __name__ == "__main__":
    log_in()