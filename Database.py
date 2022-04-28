from Indice import Indice

# Classe responsável por agir como um banco de dados contendo um único indice hash
class Database:
    def __init__(self, dados_path, pg):
        self.dados_path = dados_path
        # "Ponteiro" para a próxima linha livre que um dado vai ser adicionado
        self.next_dado = 0
        self.indice = Indice(pg)
        
        # Cria o arquivo de registros
        with open(self.dados_path, 'w') as f:
            pass

    def add_registro(self, id, rotulo, ano, tipo):
        # Adiciona ao arquivo de registros
        with open(self.dados_path, 'a') as f:
            f.write("{},{},{},{}\n".format(id, rotulo, ano, tipo))
            self.next_dado += 1

        # Adiciona ao indice
        self.indice.add_entrada(ano, self.next_dado)

    def bus_registro(self, ano):
        entradas = self.indice.bus_entrada(ano)

        with open(self.dados_path, 'r') as f:
            dados = f.readlines()
        registros = []
        for i in range(len(entradas)):
            registros.append(dados[int(entradas[i].strip().split(',')[1]) - 1])
        return registros
