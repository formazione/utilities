from random import shuffle, sample
import os




alt1 = """art.1, L'Italia è una Repubblica democratica...
art.2, La Repubblica riconosce e garantisce i diritti inviolabili dell’uomo
art.3, Tutti i cittadini hanno pari dignita` sociale
art.4, La Repubblica riconosce a tutti i cittadini il diritto al lavoro
art.5, La Repubblica - una e indivisibile - riconosce e promuove le autonomie locali
art.6, La Repubblica tutela ... le minoranze linguistiche"""

alt1 = alt1.splitlines()
qnum = len(alt1)

sol = alt1.copy()
questions = []
answers = []
for q in alt1:
	q, a = q.split(",")
	questions.append(q)
	answers.append(a)

qna = []
lettsol = []
letters = "abcd"
for n in range(qnum):
	a1 = sol[n].split(",")[1]
	pos = answers.index(a1)
	answers.pop(pos)
	shuffle(answers)
	a2, a3, a4 = sample(answers, 3)
	qq = f"Come inizia l'{questions[n]}?"
	x = [a1, a2, a3, a4]
	shuffle(x)
	right = x.index(a1)
	lettsol.append(letters[right])
	qna.append([qq, x])
	answers.insert(pos, a1)
# print(*qna, sep="\n")


def lprint(x, br=0):
	global text
	if br:
		text += "<br>"
	text += x + "<br>"

# Print the questions and answers randomized
text = ""
counter = 0
qcount = 0
for q in qna:
	q, a = q

	# PRINT QUESTION 1. What.... ?
	qcount += 1
	print(qcount, ".", q)
	q = q.replace(q, f"<b>{q}</b>")
	q = q.replace(questions[qcount-1], f"<u>{questions[qcount-1]}</u>")
	lprint(f"{qcount}.{q}", br=1)

	# PRINT MULTIPLE CHOICE a) ..... b) .....
	for ans in a:
		print(f"{letters[counter]})" + ans)
		lprint(f"{letters[counter]}){ans}")
		counter += 1
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

with open("mc.html", "w") as file:
	file.write(text)
os.startfile("mc.html")
