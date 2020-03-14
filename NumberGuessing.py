import random

while True:
    print("Ich habe mir eine Zahl ausgedacht. Kannst Du sie errraten?")
    print()
    # Zufallszahl machen
    computerZahl = random.randint(1, 100)
    zaehler = 1
    # 10 Versuche
    while zaehler <= 10:
        print("Das ist dein " + str(zaehler) + ". Versuch.")
        meineZahl = int(input("Wie lautet Deine Zahl? "))

        if meineZahl == computerZahl:
            print("Du hast die Zahl richtig erraten.")
            break
        
        if meineZahl < computerZahl:
            print("Deine Zahl ist zu niedrig.")

        if meineZahl > computerZahl:
            print("Deine Zahl ist zu hoch.")

        if zaehler == 10:
            print("Meine Zahl ist " + str(computerZahl) + ".")
        else:
            print("Rate noch einmal.")
        
        zaehler = zaehler + 1

    antwort = input("Möchtest du noch einmal spielen (ja/nein)? ")
    if antwort == "nein":
        break
