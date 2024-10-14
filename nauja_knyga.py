
nauja_knyga = []

autorius = input("Įveskite knygos autorių")
nauja_knyga.append(autorius)

pavadinimas = input("Įveskite knygos pavadinimą")
nauja_knyga.append(pavadinimas)

zanras = input("Įveskite knygos žanrą")
nauja_knyga.append(zanras)

metai = input("Įveskite knygos išleidimo metus")
nauja_knyga.append(metai)

import knygos

knygos_nr = 1
knygos_nr = 1 + knygos_nr

def prideti_knyga():
   visos_knygos[knygos_nr] = [nauja_knyga]   

print(f"Jūsų įvesta knyga {nauja_knyga} pridėta i biblioteka")


