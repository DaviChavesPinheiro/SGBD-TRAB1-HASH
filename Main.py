from Database import Database
db = Database("arquivo_de_dados.txt", 2)
db.add_registro(0, "teste", 1980, "tinto")
db.add_registro(0, "teste", 2000, "tinto")
db.add_registro(1, "teste2", 2001, "branco")