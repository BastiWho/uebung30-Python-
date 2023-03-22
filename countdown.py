import datetime
import time

osterferien = datetime.datetime(2023, 4, 11, 00, 00, 00)

while True:
    jetzt = datetime.datetime.now()

    verbleibende_zeit = osterferien - jetzt

    if verbleibende_zeit.days < 0:
        break

    stunden, reste = divmod(verbleibende_zeit.seconds, 3600)
    minuten, sekunden = divmod(reste, 60)

    print(f"Verbleibende Zeit bis zu den Osterferien: {verbleibende_zeit.days} Tage, {stunden:02d}:{minuten:02d}:{sekunden:02d}")

    time.sleep(1)


print("\nFrohe Ostern!")
print()