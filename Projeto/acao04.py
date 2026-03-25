
 
def vincular_garcom():

    """ Função para vincular o garçom à mesa, utilizando um dicionário para armazenar as informações"""
    mesas= {} 
    funcionario= int(input("Digite o ID do Funcionário: "))
    atualizar_mesa= int(input("Digite o número da mesa: "))
    mesas= {"ID":funcionario ,
              "Mesa:":atualizar_mesa      }
    return(funcionario,mesas) 


    
    