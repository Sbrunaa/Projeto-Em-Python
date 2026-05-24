from auth import register
from auth import login
from users import name_password_users

#variaveis inicializadas
option = ""


# loop de repetição para que só é verdade se for diferente de 0 caso seja inserido 0 ele encerra o programa
while option !="0":
    #menu com as opções
    print("------------------------Menu---------------------------")
    print("    Digite 1 - Cadastro.")
    print("    Digite 2 - Login.")
    print("    Digite 0 - Sair.")
    print()

    #recebe as opções
    option =  input("Escolha a opção:")  

if option =="1":
    register(name_password_users)
elif option =="2":
    login(name_password_users)


  
