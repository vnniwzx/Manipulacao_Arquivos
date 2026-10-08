def cadastrarJogador():
    nome = input("Digite seu nome: ")
    pontuacao = input("Digite sua pontuação: ")

    arquivo = open("jogadores.txt", "a")#Modo edição
    arquivo.write(nome + " - " + pontuacao + "\n")
    arquivo.close()

    print("Jogador salvo!")

def verRanking():
    jogadores = []
    arquivo = open("jogadores.txt", "r")#Modo somente leitura
    linhas = arquivo.readlines()
    arquivo.close()

    #Separar os dados (nome e pontos)
    for linha in linhas:
        partes = linha.strip().split(" - ")
        nome = partes[0]
        pontuacao = int(partes[1])

        jogadores.append((nome, pontuacao))

    #Ordenação
    jogadores.sort(key=lambda x: x[1], reverse=True)

    #Exibir o rank
    print("=== RANKING ===")

    posicao = 1

    for jogador in jogadores:
        print(posicao, "-", jogador[0], "-", jogador[1])
        posicao += 1

    print("Total de jogadores: ", len(linhas))

def buscarJogador():
    nome_busca = input("Digite o nome do jogador: ")

    arquivo = open("jogadores.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    encontrado = False

    for linha in linhas:
        if nome_busca in linha:
            print("Jogador encontrado:")
            print(linha)
            encontrado = True

    if not encontrado:
        print("Jogador não encontrado")

while True:
    print("1 - Cadastrar jogador")
    print("2 - Ver ranking")
    print("3 - Buscar Jogador")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrarJogador()
    elif opcao == "2":
        verRanking()
    elif opcao == "3":
        buscarJogador()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
