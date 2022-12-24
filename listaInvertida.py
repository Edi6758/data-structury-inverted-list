from jogador import Jogador
from diretorio import Diretorio


class listaInvertida:
    def __init__(self):
        self.__lista = []
        self.__lista_numeroDaCamiseta = []
        self.__lista_liga = []
        self.__lista_apelidoUnicoJogador = []

    def menu_principal(self):
        while True:
            print("-"*30)
            print("Menu Principal")
            print("-"*30)
            print("1 - Busca simples")
            print("2 - Busca composta")
            print("3 - Inclusão do novo jogador")
            print("4 - Remoção de um jogador")
            print("5 - Exibir todos os dados")
            print("6 - Inserir carga de dados")
            print("0 - Sair")
            escolha = input("Escolha sua opção: ")
            if escolha == '1':
                self.busca_simples()
            elif escolha == '2':
                self.busca_composta()
            elif escolha == '3':
                self.incluir_novo_elemento()
            elif escolha == '4':
                self.remover_elemento()
            elif escolha == '5':
                self.exibir_dados()
            elif escolha == '6':
                self.inserir_carga_dados()
            else:
                print("-"*30)
                print("Volte sempre!")
                print("-"*30)
                break

    def busca_simples(self):
        print("--- Busca simples ---")
        print("Você deseja realizar a busca por qual das colunas?")
        print("1 - pais do jogador, 2 - numero da camiseta, 3 - liga, 4 - apelido unico jogador")
        coluna = input("Opção escolhida: ")
        if coluna == '1':
            paisDoJogador = int(input("Digite a mátricula que deseja buscar: "))
            self.busca_por_paisDoJogador(paisDoJogador)
        elif coluna == '2':
            numeroDaCamiseta = input("Qual o numero da camiseta que você deseja pesquisar: ")
            self.busca_por_numeroDaCamiseta(numeroDaCamiseta)
        elif coluna == '3':
            liga = input("Qual liga que você deseja pesquisar: ")
            self.busca_por_liga(liga)
        elif coluna == '4':
            apelidoUnicoJogador = int(input("Qual o apelido unico do jogador que você deseja pesquisar: "))
            self.busca_por_apelidoUnicoJogador(apelidoUnicoJogador)
        else:
            print("Não foi possivel realizar a busca")
        print("-" * 30)

    def busca_composta(self):
        print("--- Busca composta ---")
        print("Você deseja realizar a busca por quais colunas?")
        print("1 - numero da camiseta do jogador, 2 - liga, 3 - apelido unico do jogador")
        coluna1 = input("Opção 1: ")
        coluna2 = input("Opção 2: ")
        diretorio1 = 0
        diretorio2 = 0
        if coluna1 == '1' and coluna2 == '2' or coluna1 == '2' and coluna2 == '1':
            numeroDaCamiseta = input("Qual numero da camiseta do jogador você deseja pesquisar: ")
            liga = input("Qual liga você deseja pesquisar: ")
            for i in self.__lista_numeroDaCamiseta:
                if i.nome == numeroDaCamiseta:
                    diretorio1 = i
            for i in self.__lista_liga:
                if i.nome == liga:
                    diretorio2 = i
            for jogador in diretorio1.lista_objetos:
                if jogador in diretorio2.lista_objetos:
                    print(f"Mátricula: {jogador.paisDoJogador}, Nome: {jogador.nome}, numero da camiseta do jogador: {jogador.numeroDaCamiseta}, liga: {jogador.liga}")
        elif coluna1 == '2' and coluna2 == '3' or coluna1 == '3' and coluna2 == '2':
            liga = input("Qual liga você deseja pesquisar: ")
            apelidoUnicoJogador = int(input("Qual apelido unico do jogador você deseja pesquisar: "))
            for i in self.__lista_liga:
                if i.nome == liga:
                    diretorio1 = i
            for i in self.__lista_apelidoUnicoJogador:
                if i.nome == apelidoUnicoJogador:
                    diretorio2 = i
            for jogador in diretorio1.lista_objetos:
                if jogador in diretorio2.lista_objetos:
                    print(f"Apelido único de jogador: {jogador.paisDoJogador}, Nome: {jogador.nome}, liga: {jogador.liga}, apelido unico do jogador: {jogador.apelidoUnicoJogador}")
        elif coluna1 == '1' and coluna2 == '3' or coluna1 == '3' and coluna2 == '1':
            numeroDaCamiseta = input("Qual numero da camiseta do jogador você deseja pesquisar: ")
            apelidoUnicoJogador = int(input("Qual apelido unico do jogador você desejap pesquisar: "))
            for i in self.__lista_numeroDaCamiseta:
                if i.nome == numeroDaCamiseta:
                    diretorio1 = i
            for i in self.__lista_apelidoUnicoJogador:
                if i.nome == apelidoUnicoJogador:
                    diretorio2 = i
            for jogador in diretorio1.lista_objetos:
                if jogador in diretorio2.lista_objetos:
                    print(f"Apelido único de jogador: {jogador.paisDoJogador}, Nome: {jogador.nome}, numero da camiseta do jogador: {jogador.numeroDaCamiseta}, apelido unico do jogador: {jogador.apelidoUnicoJogador}")
        else:
            print("Não foi possivel realizar a busca ou não existem jogadors com esses requisitos")
        print("-" * 30)

    def busca_por_paisDoJogador(self, paisDoJogador):
        for jogador in self.__lista:
            if jogador.paisDoJogador == paisDoJogador:
                print(f"Apelido único de jogador: {jogador.paisDoJogador}, Nome: {jogador.nome}, numero da camiseta do jogador: {jogador.numeroDaCamiseta}, liga: {jogador.liga}, apelido unico do jogador: {jogador.apelidoUnicoJogador}")
                return

    def busca_por_numeroDaCamiseta(self, numeroDaCamiseta):
        for diretorio in self.__lista_numeroDaCamiseta:
            if diretorio.nome == numeroDaCamiseta:
                for jogador in diretorio.lista_objetos:
                    print(f"Apelido único de jogador: {jogador.paisDoJogador}, Nome: {jogador.nome}")

    def busca_por_liga(self, liga):
        for diretorio in self.__lista_liga:
            if diretorio.nome == liga:
                for jogador in diretorio.lista_objetos:
                    print(f"Apelido único de jogador: {jogador.paisDoJogador}, Nome: {jogador.nome}")

    def busca_por_apelidoUnicoJogador(self, apelidoUnicoJogador):
        for diretorio in self.__lista_apelidoUnicoJogador:
            if diretorio.nome == apelidoUnicoJogador:
                for jogador in diretorio.lista_objetos:
                    print(f"Apelido único de jogador: {jogador.paisDoJogador}, Nome: {jogador.nome}")

    def incluir_novo_elemento(self):
        print("--- Incluir jogador ---")
        paisDoJogador = input("Digite o país de jogador do jogador: ")
        nome = input("Digite o nome do jogador: ").upper().strip()
        numeroDaCamiseta = input("numero da camiseta do jogador atual: ").upper().strip()
        liga = input("Atua em qual liga: ").upper().strip()
        apelidoUnicoJogador = input("Possui apelido unico do jogador igual a: ")
        jogador = Jogador(paisDoJogador, nome, numeroDaCamiseta, liga, apelidoUnicoJogador)
        self.__lista.append(jogador)
        print("jogador adicionado com sucesso!")
        print("-"*30)
        self.incluir_numeroDaCamiseta(jogador)
        self.incluir_liga(jogador)
        self.incluir_apelidoUnicoJogador(jogador)

    def incluir_numeroDaCamiseta(self, jogador):
        for diretorio in self.__lista_numeroDaCamiseta:
            if diretorio.nome == jogador.numeroDaCamiseta:
                diretorio.lista_id.append(jogador.paisDoJogador)
                diretorio.lista_objetos.append(jogador)
                return
        else:
            novo_diretorio = Diretorio(jogador.numeroDaCamiseta)
            novo_diretorio.lista_id.append(jogador.paisDoJogador)
            novo_diretorio.lista_objetos.append(jogador)
            self.__lista_numeroDaCamiseta.append(novo_diretorio)

    def incluir_liga(self, jogador):
        for diretorio in self.__lista_liga:
            if diretorio.nome == jogador.liga:
                diretorio.lista_id.append(jogador.paisDoJogador)
                diretorio.lista_objetos.append(jogador)
                return
        else:
            novo_diretorio = Diretorio(jogador.liga)
            novo_diretorio.lista_id.append(jogador.paisDoJogador)
            novo_diretorio.lista_objetos.append(jogador)
            self.__lista_liga.append(novo_diretorio)

    def incluir_apelidoUnicoJogador(self, jogador):
        for diretorio in self.__lista_apelidoUnicoJogador:
            if diretorio.nome == jogador.apelidoUnicoJogador:
                diretorio.lista_id.append(jogador.paisDoJogador)
                diretorio.lista_objetos.append(jogador)
                return
        else:
            novo_diretorio = Diretorio(jogador.apelidoUnicoJogador)
            novo_diretorio.lista_id.append(jogador.paisDoJogador)
            novo_diretorio.lista_objetos.append(jogador)
            self.__lista_apelidoUnicoJogador.append(novo_diretorio)

    def remover_elemento(self):
        print("--- Remover jogador ---")
        paisDoJogador = int(input("Digite a Apelido único de jogador do jogador que deseja remover: "))
        for jogador in self.__lista:
            if jogador.paisDoJogador == paisDoJogador:
                self.__lista.remove(jogador)
                print("jogador removido com sucesso!")
        print("-"*30)

    def exibir_dados(self):
        print("--- Exibir dados ---")
        for jogador in self.__lista:
            print(f"Apelido único de jogador: {jogador.paisDoJogador}, Nome: {jogador.nome}, numero da camiseta do jogador: {jogador.numeroDaCamiseta}, liga: {jogador.liga}, apelido unico do jogador: {jogador.apelidoUnicoJogador}")
        print("-"*30)

    def inserir_carga_dados(self):
        jogador = Jogador("Ney 1", "Rafael", "10", "Liga Brasileira", "Menino Ney")
        self.__lista.append(jogador), self.incluir_numeroDaCamiseta(jogador), self.incluir_liga(jogador), self.incluir_apelidoUnicoJogador(jogador)
        jogador = Jogador("Ney 2", "Jorge", "11", "Liga Europeia", "Menino Ney")
        self.__lista.append(jogador), self.incluir_numeroDaCamiseta(jogador), self.incluir_liga(jogador), self.incluir_apelidoUnicoJogador(jogador)
        jogador = Jogador("Ney 3", "Edu", "67", "LAGES", "Menino Ney")
        self.__lista.append(jogador), self.incluir_numeroDaCamiseta(jogador), self.incluir_liga(jogador), self.incluir_apelidoUnicoJogador(jogador)
        jogador = Jogador("Ney 4", "Gui", "56", "FLORIPA", "Menino Ney")
        self.__lista.append(jogador), self.incluir_numeroDaCamiseta(jogador), self.incluir_liga(jogador), self.incluir_apelidoUnicoJogador(jogador)
        jogador = Jogador("Ney 5", "Gustavo", "44", "BLUMENAU", "Menino Ney")
        self.__lista.append(jogador), self.incluir_numeroDaCamiseta(jogador), self.incluir_liga(jogador), self.incluir_apelidoUnicoJogador(jogador)
        print("Dados inseridos com sucesso!")


