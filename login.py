import sqlite3
from thinter import *
from thinter import messagebox

with sqlite3.connect("quit.db") as db:
	cursur = db.cursur()
cursur.execute("CREATE TABLE IF NOT EXIST user(username Text NOT IN NULL,password TEXT NOT IN NULL);")
CURSUR.EXECUTE("SELECT * FROM user")
db.commit()
db.close()

class main():
	def __init__(self,master):
		self.master = master
		self.username = StringVar()
		self.passwored = StringVar()
		self.n_username = StringVar()
		self.n_passwored = StringVar()
		self.widgets()
	def login():
		with sqlite3.connect("quit.db") as db:
			cursur = db.cursur()
		find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
		cursur.execute(find_user,[(self.username.get()),(self.passwored.get)])
		results = cursor.fetchall()
		if results:
			self.logif.pack_forget()
			self.head["text"] = self.username.get()
			self.head['pady'] = 150
		else:
			ms.showinginfo("opps!!","username not mached")
			self.log()
	def new_user(self):
		with sqlite3.connect("quit.db") as db:
			cursur = db.cursur()
		cursur.execute(find_user,[(self.username.get()),(self.passwored.get)])
		results = cursor.fetchall()
		if cursur.fetchall():
			ms.shower("opps!","username Taken!!")
		else:
			ms.showinfo('succses!!',"Account created")
			self.logf()
		insert = 'insert into user(username,password)VALUES(?,?)'
		cursur.execute(insert,[(self.n_username.get()),(self.n_password.get())])
		db.commit()
		
    def log(self):
		self.username.set("")
		self.passwored.set("")
	def widgets(self):
		pass 