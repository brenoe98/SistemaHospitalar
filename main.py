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


# ---------------- FUNÇÕES PACIENTES ----------------

def cadastrar_paciente(pacientes):

    paciente = {}

    print("\nCadastro de paciente")

    paciente["Nome"] = input("Digite o nome do paciente: ")
    paciente["Idade"] = int(input("Digite a idade do paciente: "))
    paciente["CPF"] = input("Digite o CPF do paciente: ")

    paciente["Histórico"] = []

    historico = input("Digite o Histórico do paciente: ")

    paciente["Histórico"].append(historico)

    for p in pacientes:

        if p["CPF"] == paciente["CPF"]:
            print("CPF já cadastrado")
            return

    pacientes.append(paciente)

    salvar_pacientes(pacientes)

    print("Paciente cadastrado com sucesso!")


def buscar_paciente(pacientes):

    busca = input("Digite o nome ou CPF para busca: ")

    encontrado = False

    for p in pacientes:

        if p["Nome"] == busca or p["CPF"] == busca:

            print(f"\nPaciente encontrado: {p}")

            encontrado = True

            break

    if not encontrado:
        print("Paciente não encontrado")


def listar_paciente(pacientes):

    if not pacientes:
        print("Paciente não encontrado")

    else:

        for p in pacientes:

            print(f"""
Nome: {p["Nome"]}
Idade: {p["Idade"]}
CPF: {p["CPF"]}

-------------------------
""")


def excluir_paciente(pacientes):

    cpf = input("Digite o CPF do paciente para remover do sistema: ")

    encontrado = False

    for p in pacientes:

        if p["CPF"] == cpf:

            pacientes.remove(p)

            salvar_pacientes(pacientes)

            print("Paciente removido com sucesso")

            encontrado = True

            break

    if not encontrado:
        print("Paciente não encontrado")


def editar_paciente(pacientes):

    busca = input("Digite o nome do paciente que sofrerá a alteração: ")

    for p in pacientes:

        if p["Nome"] == busca:

            print("Paciente encontrado")

            p["Nome"] = input("Novo nome: ")

            p["Idade"] = int(input("Nova idade: "))

            salvar_pacientes(pacientes)

            print("Paciente atualizado com sucesso")

            break


# ---------------- MENU ----------------

def entrar():

    pacientes = carregar_pacientes()

    nome = entrada_nome.get()

    menu = tk.Toplevel()

    menu.title("Menu Principal")

    menu.geometry("400x300")

    saudacao = tk.Label(
        menu,
        text=f"Olá Dr. {nome}"
    )

    saudacao.pack()

    # BOTÃO CADASTRAR
    botao_cadastrar = tk.Button(
        menu,
        text="1 - Cadastrar paciente",
        command=lambda: cadastrar_paciente(pacientes)
    )

    botao_cadastrar.pack()

    # BOTÃO BUSCAR
    botao_buscar = tk.Button(
        menu,
        text="2 - Buscar paciente",
        command=lambda: buscar_paciente(pacientes)
    )

    botao_buscar.pack()

    # BOTÃO LISTAR
    botao_listar = tk.Button(
        menu,
        text="3 - Listar pacientes",
        command=lambda: listar_paciente(pacientes)
    )

    botao_listar.pack()

    # BOTÃO EXCLUIR
    botao_excluir = tk.Button(
        menu,
        text="4 - Excluir paciente",
        command=lambda: excluir_paciente(pacientes)
    )

    botao_excluir.pack()

    # BOTÃO EDITAR
    botao_editar = tk.Button(
        menu,
        text="5 - Atualizar paciente",
        command=lambda: editar_paciente(pacientes)
    )

    botao_editar.pack()

    # BOTÃO SAIR
    botao_sair = tk.Button(
        menu,
        text="0 - Sair",
        command=menu.destroy
    )

    botao_sair.pack()


# ---------------- MAIN ----------------

janela = tk.Tk()

janela.title("Clínica Pascoal")

janela.geometry("200x100")


# TÍTULO
titulo = tk.Label(
    janela,
    text="Clínica Pascoal"
)

titulo.pack()


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

botao_confirmar.pack()


# LOOP
janela.mainloop()