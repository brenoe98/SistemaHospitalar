import json
import tkinter as tk


# ---------------- JSON ----------------

def salvar_pacientes(pacientes):

    with open("pacientes.json", "w") as arquivo:
        json.dump(pacientes, arquivo, indent=4)


def carregar_pacientes():

    try:
        with open("pacientes.json", "r") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []


# ---------------- FUNÇÃO CADASTRO ----------------

def cadastrar_paciente(pacientes, nome, idade, cpf, historico):

    paciente = {}

    paciente["Nome"] = nome
    paciente["Idade"] = idade
    paciente["CPF"] = cpf
    paciente["Histórico"] = [historico]

    for p in pacientes:

        if p["CPF"] == paciente["CPF"]:
            print("CPF já cadastrado")
            return False

    pacientes.append(paciente)

    salvar_pacientes(pacientes)

    print("Paciente cadastrado com sucesso!")

    return True


# ---------------- JANELA CADASTRO ----------------

def janela_cadastro(pacientes):

    cadastro = tk.Toplevel()

    cadastro.title("Cadastro de Paciente")

    cadastro.geometry("300x300")

    # NOME
    tk.Label(
        cadastro,
        text="Nome"
    ).pack()

    entrada_nome = tk.Entry(cadastro)

    entrada_nome.pack()

    # IDADE
    tk.Label(
        cadastro,
        text="Idade"
    ).pack()

    entrada_idade = tk.Entry(cadastro)

    entrada_idade.pack()

    # CPF
    tk.Label(
        cadastro,
        text="CPF"
    ).pack()

    entrada_cpf = tk.Entry(cadastro)

    entrada_cpf.pack()

    # HISTÓRICO
    tk.Label(
        cadastro,
        text="Histórico"
    ).pack()

    entrada_historico = tk.Entry(cadastro)

    entrada_historico.pack()

    # FUNÇÃO SALVAR
    def salvar():

        nome = entrada_nome.get()

        idade = int(entrada_idade.get())

        cpf = entrada_cpf.get()

        historico = entrada_historico.get()

        sucesso = cadastrar_paciente(
            pacientes,
            nome,
            idade,
            cpf,
            historico
        )

        if sucesso:
            cadastro.destroy()

    # BOTÃO SALVAR
    tk.Button(
        cadastro,
        text="Salvar paciente",
        command=salvar
    ).pack(pady=10)
# ---------------- janela listar ----------------

def janela_busca(pacientes):

    busca = tk.Toplevel()

    busca.title("Buscar paciente")

# ---------------- MENU ----------------

def entrar():

    pacientes = carregar_pacientes()

    nome = entrada_nome.get()

    menu = tk.Toplevel()

    menu.title("Menu Principal")

    menu.geometry("400x300")

    saudacao = tk.Label(
        menu,
        text=f"Olá Dr. {nome} o que deseja fazer?"
    )

    saudacao.pack(pady=10)

    # BOTÃO CADASTRAR
    botao_cadastrar = tk.Button(
        menu,
        text="1 - Cadastrar paciente",
        command=lambda: janela_cadastro(pacientes)
    )

    botao_cadastrar.pack(pady=5)


# BOTÃO BUSCA
    botao_busca = tk.Button(
        menu,
        text="1 - Buscar pacientes",
        command=lambda: janela_busca(pacientes)
    )

    botao_busca.pack(pady=5)


    # BOTÃO SAIR
    botao_sair = tk.Button(
        menu,
        text="0 - Sair",
        command=menu.destroy
    )

    botao_sair.pack(pady=10)


# ---------------- MAIN ----------------

janela = tk.Tk()

janela.title("Clínica Pascoal")

janela.geometry("300x200")


# TÍTULO
titulo = tk.Label(
    janela,
    text="Clínica Pascoal"
)

titulo.pack(pady=10)


# TEXTO
texto_nome = tk.Label(
    janela,
    text="Digite seu nome Dr:"
)

texto_nome.pack()


# CAMPO DIGITAÇÃO
entrada_nome = tk.Entry(janela)

entrada_nome.pack()


# BOTÃO CONFIRMAR
botao_confirmar = tk.Button(
    janela,
    text="Entrar",
    command=entrar
)

botao_confirmar.pack(pady=10)


# LOOP
janela.mainloop()