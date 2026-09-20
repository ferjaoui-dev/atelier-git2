note1 = float(input("Note 1 : "))
note2 = float(input("Note 2 : "))
note3 = float(input("Note 3 : "))

moyenne = (note1 + note2 + note3) / 3
print("Moyenne =", moyenne)

if moyenne >= 10:
    print("Resultat : admis")
else:
    print("Resultat : non admis")