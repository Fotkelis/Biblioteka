username = "Paulius"
passw = "1234567"

user_in = input("Vartotojo vardas: ")
passw_in = input("Slaptažodis: ")

#tikrinam prisijungimus, jei tinka imortuojam knygos pridejima

if user_in == username and passw == passw:
    print("Užeikite")

import nauja_knyga


if user_in == username and passw != passw:
    print("Neteisingas slaptažodis")
if user_in != username and passw == passw:
    print("Neteisingas vartotojo vardas")
if user_in != username and passw != passw:
    print("Neteisingas vartotojo vardas ir slaptažodis ")




# and pass_in == passw:
