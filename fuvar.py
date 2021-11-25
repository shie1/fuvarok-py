from sys import exit #Buildeléshez hasznos, mert magától nem importálódik
from os import system #Konzol parancsokat futtat le
from datetime import datetime #Modul dátumok értelmezéséhez

def _main():

    #Előkészítés
    try:
        csv = open("fuvar.csv", "r", encoding="utf8").read().split("\n") #Oszlopok: 0 - taxi_id; 1 - indulas; 2 - idotartam; 3 - tavolsag; 4 - viteldij; 5 - borravalo; 6 - fizetes_modja
    except FileNotFoundError:
        print("fuvar.csv nem található!")
        system("pause")
        exit()
    del csv[0]

    #3. feladat
    print(f"3. feladat: {len(csv)} fuvar")

    #4. feladat
    trips = [] #Megtett fuvarok
    for line in csv:
        columns = line.split(";")
        if(columns[0] == "6185"):
            trips.append(line)
    money = 0 #Keresett pénz
    for line in trips:
        columns = line.split(";")
        money = money + float(columns[4].replace(',','.')) + float(columns[5].replace(',','.'))
    print(f"4. feladat: {len(trips)} fuvar alatt: {money}$") #Emlékeztető: Tizedes vessző helyett pontot használok

    #5. feladat
    payments = {}
    for line in csv:
        columns = line.split(";")
        payment_type = columns[6]
        try: 
            payments[payment_type] = payments[payment_type] + 1
        except KeyError: #Ez akkor fut le amikor még nem létezik a fizetési mód a dict-ben
            payments[payment_type] = 1

    output_5 = ""
    for key in dict.keys(payments):
        output_5 = output_5 + f"\n     {key}: {payments[key]} fuvar"
    print(f"5. feladat: {output_5}")

    #6. feladat
    distance = 0
    for line in csv:
        columns = line.split(";")
        distance = distance + float(columns[3].replace(',','.'))
    print(f"6. feladat: {round(distance, 2)} km") #Nem ugyan az jön ki, mint a mintában, de a megoldás helyes, leellenőriztem

    #7. feladat
    longest = ""
    for line in csv:
        columns = line.split(";")
        if(longest == ""): #Ha még nincs mihez hasonlítani
            longest = columns
            continue

        if(columns[2] > longest[2]): #Összehasonlítja a jelenlegit, az eddig ismert leghosszabbal, ha a jelenlegi hosszab, az lesz az új leghosszabb
            longest = columns
            continue
    print(f"7. feladat: Leghosszabb fuvar:\n     Fuvar hossza: {longest[2]} másodperc\n     Taxi azonosító: {longest[0]}\n     Megtett távolság: {longest[3].replace(',','.')} km\n     Viteldíj: {longest[4]}")

    #8. feladat
    open("hibak.txt" , "w") #Ha létezne már a fájl és van benne valami, ez kitörli. Ez azért kell ide, mert a következő opennél append mode-ot használok, ami kiegészíti a fájlt, nem felülírja.
    hibak = open("hibak.txt" , "a", encoding="utf8")
    hibak.write("taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja") #Első sor
    hibahalmaz = []
    for line in csv:
        columns = line.split(";")
        if(float(columns[3].replace(',','.')) == 0):
            if(int(columns[2]) > 0) and (float(columns[4].replace(',','.')) > 0):
                hibahalmaz.append(columns)
    hibahalmaz = sorted(hibahalmaz, key = lambda row: datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")) #Hibák időrendi sorrendbe való helyezése (Eredetileg kifelejtettem)
    for columns in hibahalmaz:
        hibak.write(f"\n{';'.join(columns)}")
    hibak.close()
    print("8. feladat: hibak.txt")
    system("pause")
    exit()

if __name__ == "__main__": #Akkor fut le, ha nem importálva van a script
    _main()
