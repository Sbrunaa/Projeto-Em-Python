option = ""
users = {}

while option !="0":

    print("------------------------Menu---------------------------")
    print("    Digite 1 - Cadastro.")
    print("    Digite 2 - Login.")
    print("    Digite 0 - Sair.")
    print()
    option =  input("Escolha a opção:")  

    if option == "1":
        new_user = input("User:")
        new_password = input("Password:")

        users[new_user] = new_password
    elif option == "2":

        user =  input("User:")
        password = input("Password:")
        if user in users and users[user] == password:
            print("Usuario válido!")
        else:
            print("Usuario invalido!")

    elif option == "0":
        break
