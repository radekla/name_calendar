"""
Tento kód slouží k procvičení práce se soubory
a s knihovnou datetime. Proto sem (alespoň prozatím)
nedám ošetření vstupu od uživatele a budu předpokládat,
že uživatel zadá všechny vstupy správně ;-)
"""

from datetime import datetime

# proiteruje soubor a vrací jméno k zadanému datu
def get_date(name):
    name_day = open("svatky.csv", "r")
    for row in name_day:
        if row.__contains__(name):
            return row.split(";")[0]
            break
        else:
            pass
    name_day.close()

# proiteruje soubor a vrací datum k zadanému jménu
def get_name(date):
    name_day = open("svatky.csv", "r")
    for row in name_day:
        if row.__contains__(date):
            return row.split(";")[1]
            break
        else:
            pass
    name_day.close()

name_day = open("svatky.csv", "r")
today = datetime.now()

# vrací dnešní datum a svátek k dnešnímu datu
for row in name_day:
    if row.__contains__("{0}.{1}.".format(today.day, today.month)):
        name_today = row.split(";")[1]
        break
name_day.close()

print("Vítej v kalendáři jmen. Dnes je {0}.{1}. "
      "a svátek má {2}.\nVyber jednu z možností (pomocí čísla), co chceš zjistit:\n"
      "1 - Chci zjistit datum\n2 - Chci zjistit jméno".format(today.day, today.month, name_today))

choice = int(input("Možnost: "))

if choice == 1:
    name = input("Zadej jméno: ")
    print("{0} má svátek {1}".format(name, get_date(name)))
elif choice == 2:
    date = input("Zadej datum ve formátu d.m. (např. 6.8.): ")
    print("{0} má svátek {1}".format(date, get_name(date)))




