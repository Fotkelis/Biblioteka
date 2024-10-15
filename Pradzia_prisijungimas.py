username = "Paulius"
passw = "1234567"

user_in = input("Vartotojo vardas: ")
passw_in = input("Slaptažodis: ")

#tikrinam prisijungimus, jei tinka imortuojam knygos pridejima
import winsound

frequency = 2000
duration = 15
winsound.Beep(frequency, duration,)
winsound.Beep(frequency, duration,)
winsound.Beep(frequency, duration,)

if user_in == username and passw_in == passw:
    print("\033[1;32;40m\n")
    print(".")
    print("..")
    print("...")
    print("Užeikite")
    print("...")
    print("..")
    print(".")
    
    import antrra_pradzia_veiksmu_pasirinkimas
   

    
elif user_in == username and passw_in != passw:
    frequency = 2000
    duration = 1500
    winsound.Beep(frequency, duration) 
    print("\033[1;31;47m\n")
    print(".")
    print("..")
    print("...")
    print("Neteisingas slaptažodis")
    print("...")
    print("..")
    print(".")
    frequency = 2000
    duration = 1500
    winsound.Beep(frequency, duration) 
elif user_in != username and passw_in == passw:
    frequency = 2000
    duration = 1500
    winsound.Beep(frequency, duration) 
    print("\033[1;31;47m\n")
    print(".")
    print("..")
    print("...")
    print("Neteisingas vartotojo vardas")
    print("...")
    print("..")
    print(".")
    frequency = 2000
    duration = 1500
    winsound.Beep(frequency, duration) 
elif user_in != username and passw_in != passw:
    frequency = 2000
    duration = 1500
    winsound.Beep(frequency, duration) 
    print("\033[1;31;47m\n")
    print(".")
    print("..")
    print("...")
    print("Neteisingas vartotojo vardas ir slaptažodis ")
    print("...")
    print("..")
    print(".")
    frequency = 2000
    duration = 1500
    winsound.Beep(frequency, duration) 
