knygos_nr = 0
   
#Sarasas naujai knygai
    
nauja_knyga = []

def sukurti_knyga():
    #kuriamas unikalus knygos numeris bibliotekoje
    
    knygos_nr = knygos_nr + 1  

    
    #surenkama knyga
    autorius = input("Įveskite knygos autorių: ")
    nauja_knyga.append(autorius)

    pavadinimas = input("Įveskite knygos pavadinimą: ")
    nauja_knyga.append(pavadinimas)

    zanras = input("Įveskite knygos žanrą: ")
    nauja_knyga.append(zanras)

    metai = input("Įveskite knygos išleidimo metus: ")
    nauja_knyga.append(metai)

#zodynas knygu bibliotekai
visos_knygos = {}



#vartotojo sukurta knyga pridedama i zodyna (biblioteka)
visos_knygos[knygos_nr] = [nauja_knyga]   

#spausdinama sukurta knyga ir visos knygos bibliotekoje
print(f"Jūsų įvesta knyga {nauja_knyga} pridėta i biblioteka")
print(f"Visos knygos {visos_knygos}")


