from random import shuffle, sample
import os


'''
    this version is for answers that has the same 2 option,
    like true false or economici finanziari... etc


'''
domanda = "Che tipo di conto è "
fin = """Banca x c/c
Denaro in cassa
Debiti v/fornitori
Crediti v/clienti
Iva a credito
Iva a debito
Mutui passivi
TFR
Cambiali attive
Cambiali passive
Fondi per rischi e oneri""".splitlines()
eco = """Merci c/acquisti
Attrezzature
Interessi passivi
Stipendi e salari
Ammortamento attrezzature
Risconti attivi
Automezzi
Software
Utenze elettriche
Prodotti c/vendite
Assicurazione""".splitlines()

# alt1 = """art.1, L'Italia è una Repubblica democratica...
# art.2, La Repubblica riconosce e garantisce i diritti inviolabili dell’uomo
# art.3, Tutti i cittadini hanno pari dignita` sociale
# art.4, La Repubblica riconosce a tutti i cittadini il diritto al lavoro
# art.5, La Repubblica - una e indivisibile - riconosce e promuove le autonomie locali
# art.6, La Repubblica tutela ... le minoranze linguistiche"""

# alt1 = alt1.splitlines()
# Crea una lista con i conti associati alla risposta giusta
alt = fin + eco
shuffle(alt)
alt1 = []
for item in alt: # es. "crediti /clienti)
    print(fin)
    tipo = "finanziario" if item in fin else "economico"
    alt1.append(item + "," + tipo)
print(fin)
print(eco)
print(alt1)
qnum = len(alt1)

# Qui c'è la lista originale
sol = alt1.copy()
# divido domande e risposta esatta
questions = []
for q in alt1:
    q, a = q.split(",")
    questions.append(q)

qna = []
lettsol = []
letters = "ab"
for n in range(qnum):
    # la risposta giusta
    right = sol[n].split(",")[1]
    qq = f"{domanda}{questions[n]}?"
    x = ["finanziario", "economico"]
    if right == "finanziario":
        lettsol.append("finanziario") 
    else:
        lettsol.append("economico")
    qna.append([qq, x])
print(lettsol)
# print(*qna, sep="\n")


def lprint(x="", br=0):
    global text
    
    if br == 0:
        text += f"<td>{x}</td><tr>"
    if br == 1:
        text += f"<tr>f<td>{x}</td><tr>"
    elif br == 2:
        text += f"<td>{x}</td>"

# Print the questions and answers randomized
text = "<table>"
counter = 0
qcount = 0
for q in qna:
    q, a = q

    # PRINT QUESTION 1. What.... ?
    qcount += 1
    print(qcount, ".", q)
    q = q.replace(q, f"<b>{q}</b>")
    q = q.replace(questions[qcount-1], f"<u>{questions[qcount-1]}</u>")
    lprint(f"{qcount}.{q}", br=2)

    # PRINT MULTIPLE CHOICE 
    '''
        a)
        b)
        c)
        d)
    '''
    for ans in a:
        print(f"{letters[counter]} [{ans}]")
        lprint(f"[{letters[counter]}] {ans}", br=2)
        counter += 1
    lprint()
    counter = 0
    print()
    text += ""

# Print the solutions at the end
print("Solutions")
lprint("Solutions", br=1)
counter = 0
for ss in sol:
    q, s = ss.split(",")
    print(f"[{counter+1}.{lettsol[counter]}]", q, s)
    lprint(f"[{counter+1}.{lettsol[counter]}]{q} {s}")
    counter += 1
print("----")

with open("mctf.html", "w") as file:
    file.write(text)
os.startfile("mctf.html")
