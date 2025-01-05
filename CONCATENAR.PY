

lista_1=[50,34,2,1]
lista_2=[90,30,10,3]

def listar(lista_1,lista_2):  
    #concatenar listas 1 e 2 em nova lista
    nova_lista = lista_1+lista_2 
    print(nova_lista)

    #metodo extend() para adicionar uma lista ao final
    lista_2.extend(nova_lista)
    print(lista_2)

    #usando loops para integrar valores especificos e diferentes condições de varias listas
    lista_completa = [valor for lista in [lista_1,nova_lista,lista_2] for valor in lista]
    print(lista_completa)

    #transformando todos os numeros em string e usando um separador especifico
    lista_completa ="-".join(f'{valor}' for valor in nova_lista)#foi usado o metodo join para inserir um separador entre os elementos
    print(type(lista_completa))
    print(lista_completa)

    #formatação de lista para estrings formatadas
    hora=[1,2,2025,12,30,20]

    dia, mes, ano = str(hora[0]).zfill(2),str(hora[1]).zfill(2),str(hora[2]).zfill(2)#o metodos permite acegurar que os elementos possuam 2 digitos na composição
    data_formatada= f'{dia}-{mes}-{ano} '
    print(data_formatada)

    h,m,s= str(hora[3]).zfill(2),str(hora[4]).zfill(2),str(hora[5]).zfill(2)
    hora_formatada= f'{h}:{m}:{s}'
    print(hora_formatada)

    data_hora_formatada=[data_formatada+hora_formatada]
    print(data_hora_formatada)

    #inserindo valores em indices na lista
    data_hora_formatada.insert(1,[lista_2,lista_1])
    print(data_hora_formatada)
    for indice, elemento in enumerate(data_hora_formatada):
        print(f"Índice: {indice}, Elemento: {elemento}")

listar(lista_1,lista_2)