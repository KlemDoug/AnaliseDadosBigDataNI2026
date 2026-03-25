
funcoes_restaurante_dict = {'exibir_cardapio' :(),
 'abrir_mesa':(), 
'add_item_pedido':(), 
'vincular_garcom':(), 
'gerar_id_pedido':(), 
'buscar_pedido':(), 
'calcular_total':(), 
'finalizar_caixa':(), 
'liberar_mesa':(), 
'cumprimentos':(), 
'desconto_usuario':(), 
'status_salao':(),
'comissao_garcom':()}

funcoes_restaurante_dict['exibir_cardapio']=(cardapio)
funcoes_restaurante_dict['abrir_mesa']=(mesas_restaurante)
# funcoes_restaurante_dict['add_item_pedido']=()
# funcoes_restaurante_dict['vincular_garcom']=()
funcoes_restaurante_dict['gerar_id_pedido']=(idpedidos)
funcoes_restaurante_dict['buscar_pedido']=(id_procurado)
# funcoes_restaurante_dict['calcular_total']=()
funcoes_restaurante_dict['finalizar_caixa']=(valor_da_conta)
funcoes_restaurante_dict['liberar_mesa']=(mesapaga)
funcoes_restaurante_dict['cumprimentos']=(cliente)
funcoes_restaurante_dict['desconto_usuario']=(faz_aniversario)
funcoes_restaurante_dict['status_salao'] = (mesa1 : disponível, 
mesa2 : ocupado, 
mesa3 : ocupado, 
mesa4 : disponível, 
mesa5 : ocupado, 
mesa6 : disponível, 
mesa7 : disponível, 
mesa8 : ocupado, 
mesa9 : disponível, 
mesa10 : ocupado)
funcoes_restaurante_dict['comissao_garcom']=(gorjeta)

print(f"Dicionário após alteração:{funcoes_restaurante_dict}")

