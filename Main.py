from Database import Database
db = Database("arquivo_de_dados.txt", 2)

db.add_registro(0, "teste", 1980, "tinto")
db.add_registro(1, "teste", 2000, "tinto")
db.add_registro(0, "teste", 2004, "tinto")
db.add_registro(0, "teste", 3000, "tinto")
db.add_registro(3, "teste2", 2001, "branco")
db.add_registro(3, "teste2", 2008, "branco")

print(db.bus_registro(2002))
