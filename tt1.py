LOGIN_PADRAO = "admin"
SENHA_PADRAO = "123"
LIMITE_TENTATIVAS = 5


def fazer_login():
    tentativas_restantes = LIMITE_TENTATIVAS

    while tentativas_restantes > 0:
        print(f"\nVocê tem {tentativas_restantes} tentativa(s).")

        nome_usuario = input("Digite o usuário: ")
        senha_usuario = input("Digite a senha: ")

        if nome_usuario == LOGIN_PADRAO and senha_usuario == SENHA_PADRAO:
            print("\nLogin realizado com sucesso!")
            return True

        tentativas_restantes -= 1
        print("Usuário ou senha incorretos.")

    print("\nVocê excedeu o número máximo de tentativas.")
    time.sleep(3)
    return False


def exibir_menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Login")
        print("2 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            acesso_liberado = fazer_login()

            if acesso_liberado:
                print("\nBem-vindo à central de ajuda!")
                break
            else:
                sys.exit()

        elif escolha == "2":
            print("\nEncerrando o sistema...")
            sys.exit()

        else:
            print("⚠️ Opção inválida!")


exibir_menu()