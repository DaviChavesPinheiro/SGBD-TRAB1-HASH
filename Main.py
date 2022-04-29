import csv
from Database import Database

def read_input(file_name) :
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda line: (line.strip().split(':')[0], int(line.strip().split(":")[1])), lines))
        return lines

def search_in_csv(ano):
    registros = []
    with open('vinhos.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip header
        next(reader, None)
        for row in reader:
            if(int(row[2]) == ano):
                registros.append(row)
    return registros

########################################
db = Database("arquivo_de_dados.txt", 2)
inputs = read_input('in.txt')

with open('out.txt', 'w') as f:
    for input in inputs:
        cmd, ano = input
        registros = search_in_csv(ano)
        # registros = [[0, "teste", 2013, "tinto"], [1, "teste", 2013, "tinto"], [2, "teste", 2013, "tinto"]]
        quantidade_tuplas = len(registros)

        for registro in registros:
            if cmd == "INC":
                out_add = db.add_registro(registro[0], registro[1], int(registro[2]), registro[3])
            elif cmd == "REM":
                out_rem = db.del_registro(int(registro[2]))
            elif cmd == "BUS=":
                out_bus = db.bus_registro(int(registro[2]))
        
        if cmd == "INC":
            pg, pl = out_add 
            f.write("INC:{}/{},{},{}\n".format(ano, quantidade_tuplas, pg, pl))
        elif cmd == "REM":
            pg, pl = out_rem 
            f.write("REM:{}/{},{},{}\n".format(ano, quantidade_tuplas, pg, pl))
        elif cmd == "BUS=":
            f.write("BUS=:{}/{}\n".format(ano, out_bus))
            




