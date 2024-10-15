username = "Paulius"
passw = "1234567"

user_in = input("Vartotojo vardas")

while True:
    if user_in == username.lower(): 
        print ("Sveiki atvykę, įveskite savo slaptažodį")
    else:
        if user_in != username:    
            print ("Bandykite dar kartą")
        else:
            print ("Pabaiga")

    
    # pass_in = input("Slaptažodis")




# and pass_in == passw:
