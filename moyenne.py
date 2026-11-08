note1 = float(input("Note 1 : "))
note2 = float(input("Note 2 : "))
note3 = float(input("Note 3 : "))

moyenne = (note1 + note2 + note3) / 3
print("Moyenne =", moyenne)

if moyenne >= 10:
    print("Resultat : admis")
else:
    print("Resultat : non admis")
    
def moyenne(notes):
    return sum(notes) / len(notes)
 
def note_max(notes):
    return max(notes)
 
def note_min(notes):
    return min(notes)

def mediane(notes):
    tri = sorted(notes)
    n = len(tri)
    return tri[n // 2]
 
notes = [12, 15, 9, 18]
print("Moyenne :", moyenne(notes))
print("Note maximale :", note_max(notes))
print("Médiane :", mediane(notes))
print("Note minimale :", note_min(notes))
