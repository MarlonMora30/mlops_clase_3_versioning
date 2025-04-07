def suma(a,b):
    """suma dos numeros"""
    return a+b

def login(username:str,password:str):

    if username == "admin":
        return "Login successful"

    return "login failed"


if __name__ == '__main__':
    print(suma( 2, 3))
    print(login("admin", "admin"))


