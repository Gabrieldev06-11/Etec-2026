import random
import tkinter as tk
from tkinter import messagebox

opcoes = ['pedra', 'papel', 'tesoura']

placar_jogador = 0
placar_computador = 0
empates = 0
historico = []


def jogar(escolha1):
    global placar_jogador, placar_computador, empates

    computador = random.choice(opcoes)

    if escolha1 == computador:
        resultado = "Empate!"
        empates += 1

    elif (
        (escolha1 == 'pedra' and computador == 'tesoura') or
        (escolha1 == 'papel' and computador == 'pedra') or
        (escolha1 == 'tesoura' and computador == 'papel')
    ):
        resultado = "Você ganhou!"
        placar_jogador += 1

    else:
        resultado = "O computador ganhou!"
        placar_computador += 1

    historico.append(
        f"Você: {escolha1.capitalize()} | "
        f"Computador: {computador.capitalize()} | "
        f"{resultado}"
    )

    jogador_label.config(
        text=f"Você escolheu: {escolha1.capitalize()}"
    )

    computador_label.config(
        text=f"Computador escolheu: {computador.capitalize()}"
    )

    resultado_label.config(text=resultado)

    placar_label.config(
        text=f"PLACAR\nVocê {placar_jogador} x {placar_computador} Computador"
    )

    estatisticas_label.config(
        text=f"Vitórias: {placar_jogador}   "
             f"Derrotas: {placar_computador}   "
             f"Empates: {empates}"
    )

    atualizar_historico()


def atualizar_historico():
    historico_texto.delete("1.0", tk.END)

    for i, partida in enumerate(historico, 1):
        historico_texto.insert(
            tk.END,
            f"Rodada {i}: {partida}\n"
        )


def limpar_jogo():
    global placar_jogador, placar_computador, empates, historico

    placar_jogador = 0
    placar_computador = 0
    empates = 0
    historico = []

    jogador_label.config(text="Você escolheu: -")
    computador_label.config(text="Computador escolheu: -")
    resultado_label.config(text="Faça sua escolha!")

    placar_label.config(
        text="PLACAR\nVocê 0 x 0 Computador"
    )

    estatisticas_label.config(
        text="Vitórias: 0   Derrotas: 0   Empates: 0"
    )

    atualizar_historico()


def mostrar_regras():
    messagebox.showinfo(
        "Regras",
        "Pedra ganha de Tesoura.\n"
        "Tesoura ganha de Papel.\n"
        "Papel ganha de Pedra.\n\n"
        "Se os dois escolherem a mesma opção, é empate."
    )


def sair():
    resposta = messagebox.askyesno(
        "Sair do jogo",
        "Tem certeza que deseja sair?"
    )

    if resposta:
        janela.destroy()


janela = tk.Tk()
janela.title("Pedra, Papel ou Tesoura")
janela.geometry("650x700")
janela.resizable(False, False)
janela.configure(bg="#202124")


titulo = tk.Label(
    janela,
    text="PEDRA, PAPEL OU TESOURA",
    font=("Arial", 24, "bold"),
    bg="#202124",
    fg="white"
)
titulo.pack(pady=20)


subtitulo = tk.Label(
    janela,
    text="Escolha uma opção para jogar!",
    font=("Arial", 14),
    bg="#202124",
    fg="#cccccc"
)
subtitulo.pack(pady=5)


botoes_frame = tk.Frame(
    janela,
    bg="#202124"
)
botoes_frame.pack(pady=20)


botao_pedra = tk.Button(
    botoes_frame,
    text="🪨\nPEDRA",
    font=("Arial", 14, "bold"),
    width=12,
    height=4,
    command=lambda: jogar("pedra")
)
botao_pedra.grid(row=0, column=0, padx=8)


botao_papel = tk.Button(
    botoes_frame,
    text="📄\nPAPEL",
    font=("Arial", 14, "bold"),
    width=12,
    height=4,
    command=lambda: jogar("papel")
)
botao_papel.grid(row=0, column=1, padx=8)


botao_tesoura = tk.Button(
    botoes_frame,
    text="✂️\nTESOURA",
    font=("Arial", 14, "bold"),
    width=12,
    height=4,
    command=lambda: jogar("tesoura")
)
botao_tesoura.grid(row=0, column=2, padx=8)


jogador_label = tk.Label(
    janela,
    text="Você escolheu: -",
    font=("Arial", 13),
    bg="#202124",
    fg="white"
)
jogador_label.pack(pady=5)


computador_label = tk.Label(
    janela,
    text="Computador escolheu: -",
    font=("Arial", 13),
    bg="#202124",
    fg="white"
)
computador_label.pack(pady=5)


resultado_label = tk.Label(
    janela,
    text="Faça sua escolha!",
    font=("Arial", 20, "bold"),
    bg="#202124",
    fg="#00ff88"
)
resultado_label.pack(pady=15)


placar_label = tk.Label(
    janela,
    text="PLACAR\nVocê 0 x 0 Computador",
    font=("Arial", 18, "bold"),
    bg="#202124",
    fg="white"
)
placar_label.pack(pady=10)


estatisticas_label = tk.Label(
    janela,
    text="Vitórias: 0   Derrotas: 0   Empates: 0",
    font=("Arial", 12),
    bg="#202124",
    fg="#cccccc"
)
estatisticas_label.pack(pady=5)


historico_titulo = tk.Label(
    janela,
    text="HISTÓRICO",
    font=("Arial", 14, "bold"),
    bg="#202124",
    fg="white"
)
historico_titulo.pack(pady=(15, 5))


historico_texto = tk.Text(
    janela,
    width=70,
    height=8,
    font=("Arial", 10),
    bg="#303134",
    fg="white"
)
historico_texto.pack(pady=5)


botoes_inferiores = tk.Frame(
    janela,
    bg="#202124"
)
botoes_inferiores.pack(pady=15)


botao_novo = tk.Button(
    botoes_inferiores,
    text="🔄 Novo jogo",
    font=("Arial", 11, "bold"),
    width=14,
    command=limpar_jogo
)
botao_novo.grid(row=0, column=0, padx=5)


botao_regras = tk.Button(
    botoes_inferiores,
    text="📖 Regras",
    font=("Arial", 11, "bold"),
    width=14,
    command=mostrar_regras
)
botao_regras.grid(row=0, column=1, padx=5)


botao_sair = tk.Button(
    botoes_inferiores,
    text="🚪 SAIR",
    font=("Arial", 11, "bold"),
    width=14,
    command=sair
)
botao_sair.grid(row=0, column=2, padx=5)


janela.mainloop()