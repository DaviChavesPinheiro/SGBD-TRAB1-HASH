import os
# Classe responsável por representar um Indice Hash (Diretorio + Buckets)
class IHash:
    def __init__(self, profundidade_global):
        self.profundidade_global = profundidade_global
        self.diretorio = []
        
        # Cria uma pasta para guardar os buckets (apenas para organizacão)
        if(not os.path.exists("./buckets")):
            os.mkdir("./buckets")

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

        if(len(lines) < 32):
            # Adiciona uma entrada e escreve no disco
            lines.append("{},{}\n".format(ano, referencia))
            with open("./buckets/{}.txt".format(posicao_diretorio), 'w') as f:
                f.writelines(lines)
        else:
            print("fazer split")
        
        
