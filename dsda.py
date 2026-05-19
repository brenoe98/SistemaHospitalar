# ----------- MAIN -----------
print("-------------clinica Pascoal-------------")

nomedr = input("Digite seu nome Dr: ")
print(f"Olá {nomedr}")

pacientes = carregar_pacientes()

while True:
    print("\n1 - Cadastrar paciente")
    print("2 - Buscar paciente")
    print("3 - Listar pacientes")
    print("4 - Excluir um paciente")
    print("5 - Atualizar um paciente")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_paciente(pacientes)

    elif opcao == "2":
        buscar_paciente(pacientes)

    elif opcao == "3":
        listar_paciente(pacientes)

    elif opcao == "4":
        excluir_paciente(pacientes)

    elif opcao == "5":
        editar_paciente(pacientes)

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida")