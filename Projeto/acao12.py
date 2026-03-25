#lista de mesas
mesa1 : disponível
mesa2 : ocupado
mesa3 : ocupado
mesa4 : disponível
mesa5 : ocupado
mesa6 : disponível
mesa7 : disponível
mesa8 : ocupado
mesa9 :disponível
mesa10 :ocupado
def listar_mesas():
print("lista de mesas:")
for numero, status in mesas.items():
print(f"mesa {numero}:{status}")
listar_mesas():
atualizar_status(numero,novo_status):