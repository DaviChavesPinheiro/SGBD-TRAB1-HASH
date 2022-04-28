from IHash import IHash

# Classe responsável por agir como um banco de dados contendo um único indice hash
class Database:
    def __init__(self, arquivo_de_dados, profundidado_global):
        self.arquivo_de_dados = arquivo_de_dados
        # "Ponteiro" para a próxima linha livre que um dado vai ser adicionado
        self.next_dado = 0
        self.i_hash = IHash(profundidado_global)

        with open(self.arquivo_de_dados, 'w') as f:
            pass
    def add_registro(self, id, rotulo, ano, tipo):
        # Adiciona ao arquivo de dados
        with open(self.arquivo_de_dados, 'a') as f:
            f.write("{},{},{},{}\n".format(id, rotulo, ano, tipo))
            self.next_dado += 1

        # Adiciona ao indice
        self.i_hash.add_entrada(ano, self.next_dado)
