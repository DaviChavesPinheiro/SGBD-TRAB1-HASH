import os
from Page import Page
# Classe responsável por representar um Indice Hash (Diretorio + Buckets)
class Indice:
    def __init__(self, pg):
        self.pg = pg
        self.diretorio = []
        
        # Cria uma pasta para guardar os buckets (apenas para organizacão)
        if(not os.path.exists("./buckets")):
            os.mkdir("./buckets")
        
        # Deleta os buckets antigos
        for i in os.listdir("./buckets"):
            os.remove("./buckets/" + i)

        # Cria os 4 buckets iniciais
        for i in range(2 ** pg):
            # No diretorio, será armazenado apenas a profundidade local
            self.diretorio.append(pg)
            Page.data = []
            Page.write("./buckets/{}.txt".format(i))
            
    def add_entrada(self, ano, p_registro):
        hs = hash(ano)
        # Indice do diretorio. ex: (1980 % 4 = 0) == (11110111100 % 100 = 00)
        index = hs % (2 ** self.pg)
        
        # Lê o bucket
        Page.read("./buckets/{}.txt".format(index))
        bucket = Page.data
        
        # Remove possiveis linhas vazias
        bucket = list(filter(lambda line: line.strip() != "", bucket))

        # Adiciona uma entrada
        bucket.append("{},{}\n".format(ano, p_registro))
                    
        # Salva o bucket
        Page.data = bucket
        Page.write("./buckets/{}.txt".format(index))

        # Se o bucket está cheio
        # TODO: MUDAR PARA 32
        if(len(bucket) == 3):
            prf_local = self.diretorio[index]

            if(prf_local == self.pg):
                self.duplicar_diretorio()
                self.pg += 1
            
            # Cria um novo bucket e linka o diretorio
            index_novo = index + 2 ** prf_local
            
            self.diretorio[index] += 1
            self.diretorio[index_novo] += 1

            Page.data = []
            Page.write("./buckets/{}.txt".format(index_novo))
            
            # Redistribui as entradas do bucket cheio
            # TODO: MUDAR PARA 32
            for i in range(3):
                # Lê o bucket cheio
                Page.read("./buckets/{}.txt".format(index))
                bucket = Page.data

                info = bucket[i].strip().split(',')
                ano = int(info[0])
                p_registro = int(info[1])
                
                # Se a entrada deveria estar no novo bucket
                if(hash(ano) % (2 ** self.pg) != index):
                    bucket[i] = "\n"
                    Page.data = bucket
                    Page.write("./buckets/{}.txt".format(index))
                    
                    # Faz uma chamada recursiva para alocar a entrada no novo bucket
                    self.add_entrada(ano, p_registro)
    
    # Duplica o diretorio atual        
    def duplicar_diretorio(self):
        for i in range(2 ** self.pg, 2 ** (self.pg + 1)):
            self.diretorio.append(self.pg)

    def bus_entrada(self, ano):
        hs = hash(ano)
        # Indice do diretorio. ex: (1980 % 4 = 0) == (11110111100 % 100 = 00)
        index = hs % (2 ** self.pg)
        
        # Lê o bucket
        Page.read("./buckets/{}.txt".format(index))
        bucket = Page.data
        # Remove as linhas vazias
        bucket = list(filter(lambda line: line.strip() != "", bucket))
        # Retorna as entradas que possuem ano X
        return list(filter(lambda line: int(line.split(',')[0]) == ano, bucket))
   
    def del_entrada(self, ano):
        hs = hash(ano)
        # Indice do diretorio. ex: (1980 % 4 = 0) == (11110111100 % 100 = 00)
        index = hs % (2 ** self.pg)
        
        # Lê o bucket
        Page.read("./buckets/{}.txt".format(index))
        bucket = Page.data
        # Remove as linhas vazias
        bucket = list(filter(lambda line: line.strip() != "", bucket))
        # Filtra as entradas que vão ser deletadas
        del_entradas = list(filter(lambda line: int(line.split(',')[0]) == ano, bucket))
        # Remove as entradas que devem ser deletadas
        bucket = list(filter(lambda line: int(line.split(',')[0]) != ano, bucket))
        # Salva no bucket
        Page.data = bucket 
        Page.write("./buckets/{}.txt".format(index))

        return del_entradas

