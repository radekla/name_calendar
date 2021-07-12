"""
Tento kód slouží k procvičení práce se soubory
a s knihovnou datetime. Proto sem (alespoň prozatím)
nedám ošetření vstupu od uživatele a budu předpokládat,
že uživatel zadá všechny vstupy správně ;-)
"""

from datetime import datetime

# proiteruje soubor svatky.csv a vrátí požadované jméno nebo datum
def get_data(choice):
    option = {1: 0, 2: 1}
    data = {1: "jméno", 2: "datum"}
    with open("svatky.csv", "r") as name_day:
        insert = input("Zadej {0}: ".format(data[choice]))

        # přidá záznam do logu
        with open("logs.txt", "a") as record:
            record.write(insert + "\n")

        for row in name_day:
            if row.__contains__(insert):
                return row.split(";")[option[choice]]

# vrací dnešní datum a svátek k dnešnímu datu
with open("svatky.csv", "r") as name_day:
    today = datetime.now()
    for row in name_day:
        if row.__contains__("{0}.{1}.".format(today.day, today.month)):
            name_today = row.split(";")[1]
            break

print("Vítej v kalendáři jmen. Dnes je {0}.{1}. "
      "a svátek má {2}.\nVyber jednu z možností (pomocí čísla), co chceš zjistit:\n"
      "1 - Chci zjistit datum\n2 - Chci zjistit jméno".format(today.day, today.month, name_today))

choice = int(input("Možnost: "))

print("\nTady máš informaci, kterou jsi chtěl: {0}".format(get_data(choice)))



