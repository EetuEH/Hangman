import random
import json

def tallennaPeli(pelaaja):
    with open("tallennus.json","w") as f:
        json.dump(pelaaja,f)

def lataaPeli():
    pelaaja = None
    with open("tallennus.json") as f:
        pelaaja = json.load(f)

    return pelaaja

def arvoSana():
    with open("../Harjoitustyo/sanoja.txt") as word_file:
        sanat = word_file.read().split()
    arvottuSana = random.choice(sanat)
    return arvottuSana
    #käytä tätä tallentamalla johonkin muuttujaan "arvoSana()"

def peli(pelaaja):
    #peli alkaa tästä.
    symboli = "_"
    while symboli in pelaaja['PiilotettuSana'] and pelaaja['Arvaustenmaara']<6:
        print(pelaaja['PiilotettuSana'])
        arvaus = str(input("Arvaa kirjain: ")[0])
        if arvaus in pelaaja['ArvattavaSana']:
            print("")
            print("Oikea arvaus!")
            print("")
            indeksit = ([pos for pos, char in enumerate(pelaaja['ArvattavaSana']) if char == arvaus])
            #ylempi listakomprehensio antaa kaikki indeksit joista löytyy
            #pelaajan arvaama kirjain ja laittaa ne listaan nimeltä indeksit
            for ind in indeksit:
                pelaaja['PiilotettuSana'][ind] = arvaus
            
            tallennaPeli(pelaaja)
        else:
            print("")
            print("Väärä arvaus!")
            print("")
            pelaaja['Arvaustenmaara'] = pelaaja['Arvaustenmaara'] + 1
            tallennaPeli(pelaaja)
    if pelaaja['Arvaustenmaara'] == 6:
        print(" +---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("     |")
        print("    ===")
        print("")
        print("Hävisit pelin. Sana oli:", pelaaja['ArvattavaSana'])
        #nollataan seuraavaksi pelaaja ja tallennetaan peli
        pelaaja['Nimi'] = None
        pelaaja['Arvaustenmaara'] = None
        pelaaja['ArvattavaSana'] = None
        pelaaja['PiilotettuSana'] = None
        pelaaja['ArvatutKirjaimet'] = None
        pelaaja = None
        tallennaPeli(pelaaja)
        print("")
        input("Paina enteriä poistuaksesi pelistä")
        #Tämä input on laitettu sen takia, ettei peli sulkeutuisi heti päätyttyään.(kyseinen asia tapahtuu vain komentorivin kautta pelattaessa)
    else:
        print("\_0_/")
        print("  |")
        print(" / \ ")
        print("")
        print("Voitit pelin! Arvasit sanan, joka oli:", pelaaja['ArvattavaSana'])
        #nollataan seuraavaksi pelaaja ja tallennetaan peli
        pelaaja['Nimi'] = None
        pelaaja['Arvaustenmaara'] = None
        pelaaja['ArvattavaSana'] = None
        pelaaja['PiilotettuSana'] = None
        pelaaja['ArvatutKirjaimet'] = None
        pelaaja = None
        tallennaPeli(pelaaja)
        print("")
        input("Paina enteriä poistuaksesi pelistä")
#Alkuruutu
print("Tervetuloa pelaamaan hirsipuuta!")
print("")
pelaaja = None
if input("Ladataanko peli? (K , E)") == "K":
    try:
        pelaaja = lataaPeli()
    except:
        print("lataus epäonnistui")
        pelaaja = None      
    
if pelaaja == None:
    pelaaja = {'Nimi': "",
               'Arvaustenmaara': 0,
               'ArvattavaSana': "",
               'PiilotettuSana': [],
               'ArvatutKirjaimet': []
               }
    pelaaja['ArvattavaSana'] = arvoSana()
    pelaaja['PiilotettuSana'] = ["_" for x in range(len(pelaaja['ArvattavaSana']))]
    pelaaja['Nimi'] = input("Kerro nimesi: ")
    print("Tsemppiä", pelaaja['Nimi'])

peli(pelaaja)
