from utils import isValid_age

users_db={
    "admin123":{
        "name": "jhon",
        "age":34,
        "user name":"admin123",
        "password": "123",
        "rol":"admin"
    },
}

def verify_user_name():
    while True:
        try:
            user_name=input("your user name: ")
            if user_name in users_db:
                raise ValueError(f"{user_name} already exists, try again.")
            else:
                return user_name
        except ValueError as e:
            print("Error", e)


def create_count():
    name=input("fullname: ")
    age=isValid_age()
    user_name=verify_user_name()
    password=input("password: ")
    
    if not user_name in users_db:
        confirm_created=input("create count? (yes/not): ").lower()
        if confirm_created == "yes":
            users_db[user_name] = {
            "name": name,
            "age":age,
            "user name":user_name,
            "password": password,
            "rol":"user"
            }
            print("successfully created")
        elif confirm_created == "not":
            print("okey....")
        else:
            print("data invalid")
            
def change_password():
    credencials=verify_user_name()
    new_password=input("your new password: ")
    print(credencials)
        