while True:
    print("Sveiki, pasirinkite veiksmą: \n 1 - Pridėti naują knygą \n 2 - Pašalinti knygą \n 3 - Pasiimti knygą \n 4 - Ieškoti knygos \n 5 - Peržiūrėti visas knygas \n 6 - Peržiūrėti vėluojančias knygas \n 7 - Išeiti iš programos")

    userin_1 = input()
    
    if userin_1 == "1":
        import nauja_knyga

    if userin_1 == "7":
        break
       

    else:
        print("\033[1;32;41m")
        print("Bandykite dar kartą")
        print("\033[1;30;40m")  
print("\033[1;30;40m")        