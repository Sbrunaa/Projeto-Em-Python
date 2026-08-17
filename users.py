name_password_users = {}
arquivo = open("users.txt","r")

linhas = arquivo.readlines()

for linha in linhas:
    linha = linha.strip()

    users, password = linha.split(",")
    name_password_users[users] = password
arquivo.close()

