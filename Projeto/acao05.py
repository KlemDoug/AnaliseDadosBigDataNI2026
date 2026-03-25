# forma de lista 
def gerar_id_pedido(lista_de_pedidos):
    from random import randint
    idpedidos=[]
    for i in range(len(lista_de_pedidos)):
        novoid=randint(100,500)
        if novoid not in idpedidos:
            idpedidos.append(novoid)
    for j in range(len(lista_de_pedidos)):
        print(f'{lista_de_pedidos[j]} correspnde ao id:{idpedidos[j]}')
#forma dicionario 
      
def gerar_id_pedido(listas_de_pedidos):
    from random import randint
    idpedido = {}
    idlist = []
    cont=0
    while len(idlist) < len(listas_de_pedidos):
        novoid = randint(100, 500)
        if novoid not in idlist:
            idlist.append(novoid)
            cont+=1
    for i in range(len(listas_de_pedidos)):
        item = listas_de_pedidos[i]
        iditem = idlist[i]
        idpedido[item] = iditem
    print("Dicionário Gerado:", idpedido)
