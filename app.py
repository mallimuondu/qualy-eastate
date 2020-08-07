import sqlite3
import datetime as time
conn = sqlite3.connect('tryall.db')
now = time.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Good night.')
    
    
activites  = input("""
choose which activity you want
a.veiw
b.add 
c.exit
want to do:  
""")
if activites ==  "1" or activites == "a":
    name = input("enter your name: ")
    print(name)
#    print(name)
    c.execute('CREATE TABlE  IF NOT EXISTS  add(name TEXT)')
    c.execute('INSERT INTO add(bane) VALUES(?)',(name))
    
elif activites == '2':
    c.execute("SELECT * FROM odinary  ")
#    for a in c.fetchall():
#         print(a + name)
else:
    print("Error")