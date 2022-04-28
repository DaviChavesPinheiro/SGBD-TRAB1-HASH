import os
# Classe responsável por representar um Indice Hash (Diretorio + Buckets)
class IHash:
    def __init__(self, profundidade_global):
        self.profundidade_global = profundidade_global
        self.diretorio = []
        
        # Cria uma pasta para guardar os buckets (apenas para organizacão)
        if(not os.path.exists("./buckets")):
            os.mkdir("./buckets")
        
        # Deleta os buckets antigos
        for i in os.listdir("./buckets"):
            os.remove("./buckets/" + i)

        for i in range(2 ** profundidade_global):
            # No diretorio, será armazenado o indice "binário" + a profundidade local
            # Isso é reduntante, pois o indice do array corresponde ao indice do bucket, mas vou deixar assim.
            self.diretorio.append((i, profundidade_global))
            with open("./buckets/{}.txt".format(i), "w") as f:
                pass
            
    
    # Referencia é a linha do arquivo de dados
    def add_entrada(self, ano, referencia):
        hs = hash(ano)
        # Indice do diretorio. ex: (1980 % 4 = 0) == (11110111100 % 100 = 00)
        posicao_diretorio = hs % (2 ** self.profundidade_global)
        
        # Lê toda a página
        with open("./buckets/{}.txt".format(posicao_diretorio), 'r') as f:
            lines = f.readlines()
            print(lines)
        
        # TODO: MUDAR PARA 32
        if(len(lines) < 3):
            # Adiciona uma entrada e escreve no disco
            lines.append("{},{}\n".format(ano, referencia))
            with open("./buckets/{}.txt".format(posicao_diretorio), 'w') as f:
                f.writelines(lines)
        else:
            _, prf_atual = self.diretorio[posicao_diretorio]
            if(prf_atual + 1 > self.profundidade_global):
                self.duplicar_diretorio()
            index_bucket, index_bucket_novo = self.duplicar_bucket(posicao_diretorio)

            # Incrementa a profundidade local dos dois buckets
            _, prf_atual = self.diretorio[index_bucket]
            self.diretorio[index_bucket] = (index_bucket, prf_atual + 1)
            self.diretorio[index_bucket_novo] = (index_bucket_novo, prf_atual + 1)
            print(self.diretorio)
    
    # Duplica o diretorio atual        
    def duplicar_diretorio(self):
        for i in range(2 ** self.profundidade_global, 2 ** (self.profundidade_global + 1)):
            self.diretorio.append((i, self.profundidade_global))
        self.profundidade_global += 1
    
    # Duplica o bucket e altera a referencia do diretorio 
    def duplicar_bucket(self, index_bucket):
        # Index do bucket que vai ser duplicado (split)
        index, prf_local = self.diretorio[index_bucket]
        
        # Index do novo bucket
        index_novo = index_bucket + 2 ** prf_local
        index_novo, prf_local_novo = self.diretorio[index_novo]
        
        # Cria o bucket novo
        with open("./buckets/{}.txt".format(index_novo), 'w') as f:
            pass
        
        # Retorna o index do bucket antigo e do novo
        return (index, index_novo)




