def register(name_password_users):
    new_user = input("User:").strip()

    #o while se repetir até que seja inserido um usuario que não exixte ainda e não esteja vazio
    while new_user == "" or new_user in name_password_users:
        if new_user =="":
            print("O usuario não pode ficar em branco!")
        else:
            print("Usuario já exixte!")

        new_user = input("User:").strip()

        #valida a senha , verificando se nao esta vazia
        new_password = input("Password:").strip()
    while new_password == "":
        print("A senha não pode ficar em branco!")
        new_password = input("Password:").strip()

        #cria o usuario depois das validações  
    name_password_users[new_user] = new_password
    print("Usuario cadastrado com sucesso!")

def login(name_password_users):
     
    #entrada do usuario
    user =  input("User:").strip()

    #valida se não eta vazia a entrada
    while user == "":
        print("A user não pode ficar em branco!")
        user = input("User:").strip()

    #entrada da senha
    password = input("Password:").strip()

    #valida se não eta vazia a entrada
    while password == "":
        print("A senha não pode ficar em branco!")
        password = input("Password:").strip()
    
    #verifica se o usuario é valido se esta no dicionario de usuarios cadastrados
    if user in name_password_users and name_password_users[user] == password:
        print("Usuario válido!")
    else:
        print("Usuario invalido!")



