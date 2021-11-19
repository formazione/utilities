import smtplib

def tkinput(text) -> str:
	import tkinter as tk

	root = tk.Tk()
	question = tk.StringVar()
	tk.Label(root, text=text).pack()
	e = tk.Entry(root, textvariable=question)
	e.pack()
	e.focus()
	# question.set("prova")
	e.bind("<Return>", lambda event: root.destroy())
	root.mainloop()
	return question.get()



if __name__ == '__main__':
	host = "smtp.gmail.com"
	mmail = tkinput("Your mail")
	hmail = tkinput("Send mail to")
	subject = tkinput("subject")
	text = tkinput("text")
	server = smtplib.SMTP(host, 587)
	server.ehlo()
	server.starttls()
	''' if you have 2 factor authentication on gmail
	1. Log-in into Gmail with your account
	2. Navigate to https://security.google.com/settings/security/apppasswords
	3. In 'select app' choose 'custom', give it an arbitrary name and press generate
	4. It will give you 16 chars token.
	'''
	# my token to send mail
	# ....
	# smtp.pelconsip.aruba.it
	password = tkinput("Password:")
	# errore second factor
	server.login(mmail, password)
	server.sendmail(mmail, [hmail], text)
	server.quit()
	

