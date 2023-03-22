frage = input("Funktioniert das System? [j/n] ")

if frage == "j":
    print("Fummel nicht daran herum! Alles ist gut.")
else:
    guilty = input("Bist du Schuld? [j/n] ")
    if guilty == "n":
        print("Dich trifft es nicht!")
    else:
        print("Du bist ein Idiot!")
        recog = input("Hat es jemand gemerkt? [j/n] ")
        if recog == "n":
            print("Man wird dich nie finden!")
        else:
            print("Du bist am Arsch!")
            guilt2 = input("Kannst du jemand anderem die Schuld zuschieben? [j/n] ")
            if guilt2 == "n":
                print("Du bist wirklich am Arsch!")
            else:
                print("Keine Sorge, jemand anderes ist am Arsch!")