from usuario import cadastrar_usuario, login

def menu():
    while True:
        print("\n== SISTEMA DE LOGIN ==")
        print("[1] Cadastrar")
        print("[2] Login")
        print("[3] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            cadastrar_usuario(nome, email, senha)
        elif opcao == "2":
            email = input("Email: ")
            senha = input("Senha: ")
            login(email, senha)
        elif opcao == "3":
            break
        else:
            print("Opção invalida!")

menu()