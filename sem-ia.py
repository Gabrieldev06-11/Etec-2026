import random

opcoes = ['pedra', 'papel', 'tesoura']

placar_jogador=0
placar_computador=0

while True:
    escolha1 = input("Digite Pedra, Papel ou Tesoura (ou 'sair' para encerrar):").strip().lower()
    if escolha1 == 'sair':

        print("Jogo encerrado!")
        break
    if escolha1 not in opcoes:

        print("Opção inválida! Digite apenas Pedra, Papel ou Tesoura.\n")

    else:

        print(f"Você escolheu: {escolha1.capitalize()}\n")

    computador = random.choice (opcoes)
    print(f"O computador escolheu: {computador.capitalize()}\n")

    if escolha1 == computador:

        print("Empate!\n")
    elif (escolha1 == 'pedra' and computador == 'tesoura') or \
    (escolha1 == 'papel' and computador == 'pedra') or \
    (escolha1 == 'tesoura' and computador == 'papel'):
        print("Você ganhou!\n")

        placar_jogador +=1
    else:
        print("O computador ganhou!\n")
        placar_computador +=1



    print(f"PLACAR ATUAL: Você {placar_jogador} x {placar_computador} Computador\n")