import sqlite3
conn = sqlite3.connect('nesh.db')
c = conn.cursor()
activeties  = input("""
choose which activity you want
a.veiw
b.add 
c.exit
want to do:  
""")
if activeties == "a":
    name = input("enter your name: ")
    age = input("Enter yur age: ")
    print(name)
    c.execute('CREATE TABLE IF NOT EXISTs names(name TEXT, age INTEGER)')
    c.execute('INSERT INTO names(name,age) VALUES(?,?)',(name,age))

elif activeties == "b":
    c.execute('SELECT * FROM names')
    data = c.fetchall()
    for dub in data:
        print(dub)
else:
    print("goodbye")
#    print(name)
#    c.execute('CREATE TABlE  IF NOT EXISTS  add(name TEXT)')
#    c.execute('INSERT INTO add(bane) VALUES(?)',(name))
        