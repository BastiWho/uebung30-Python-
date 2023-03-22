print("\n Berechnen wir dch mal das Schaltjahr")
print("---------------------------------------\n")
jahr = int(input("Welches Jahr möchtest du überprüfen? "))
print()
if jahr % 4 == 0:
    if jahr % 100 == 0:
        if jahr % 400 == 0:
            print("Das Jahr",jahr, "ist ein Schaltjahr.")
        else:
            print("Das Jahr",jahr, "ist kein Schaltjahr.")
    else:
        print("Das Jahr",jahr, "ist ein Schaltjahr.")
else:
    print("Das Jahr",jahr, "ist kein Schaltjahr.")

print("\nDas wars! Danke fürs da sein :).")
print("==================================")