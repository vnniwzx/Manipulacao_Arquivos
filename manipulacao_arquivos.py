def cadastrarJogador():
    nome = input("Digite seu nome: ")
    pontuacao = input("Digite sua pontuação: ")

    arquivo = open("jogadores.txt", "a")#Modo edição
    arquivo.write(nome + " - " + pontuacao + "\n")
    arquivo.close()

    print("Jogador salvo!")

def verRanking():
    arquivo = open("jogadores.txt", "r")#Modo somente leitura
    linhas = arquivo.readlines()
    arquivo.close()

    print("=== RANKING ===")

    for linha in linhas:
        print(linha)

while True:
    print("1 - Cadastrar jogador")
    print("2 - Ver ranking")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrarJogador()
    elif opcao == "2":
        verRanking()
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
