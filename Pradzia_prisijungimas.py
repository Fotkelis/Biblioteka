

username = "Paulius"
passw = "1234567"

user_in = input("Vartotojo vardas: ")
passw_in = input("Slaptažodis: ")

#tikrinam prisijungimus, jei tinka imortuojam knygos pridejima

if user_in == username and passw == passw:
    print("\033[1;32;40m\n")
    print(".")
    print("..")
    print("...")
    print("Užeikite")
    print("...")
    print("..")
    print(".")

    import nauja_knyga



elif user_in == username and passw != passw:
    print("\033[1;31;47m\n")
    print(".")
    print("..")
    print("...")
    print("Neteisingas slaptažodis")
    print("...")
    print("..")
    print(".")
elif user_in != username and passw == passw:
    print("\033[1;31;47m\n")
    print(".")
    print("..")
    print("...")
    print("Neteisingas vartotojo vardas")
    print("...")
    print("..")
    print(".")
elif user_in != username and passw != passw:
    print("\033[1;31;47m\n")
    
    print(".")
    print("..")
    print("...")
    print("Neteisingas vartotojo vardas ir slaptažodis ")
    print("...")
    print("..")
    print(".")