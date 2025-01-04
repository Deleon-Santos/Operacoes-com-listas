"""Calculando soma de valores em Listas"""

valor_gasto=[50,34,2,1]
valor_recebido=[90,30,10,3]

def listar(valor_gasto,valor_recebido):
    total_gasto, total_entrada = float(sum(valor_gasto)),float(sum(valor_recebido))
    saldo = total_entrada-total_gasto
    return saldo, total_entrada, total_gasto

while True:
    resultados=listar(valor_gasto,valor_recebido)
    option = input('\nTipo de consulta\n1-saldo \n2-entradas \n3-gastos\n0-sair \n>> ')
    if option == '0':
        break
    elif option == '1':
        print(f'O saldo total da conta é R$ {resultados[0]:.2f}')
    elif option == '2':
        print(f'Valor recebido: R$ {resultados[1]:.2f}')
    elif option == '3':
        print(f'Valor gasto: R$ {resultados[2]:.2f}')
    else:
        print('Opção inválida')
print(f"O saldo total da conta é R$ {resultados[2]:.2f} Valor gasto: R$ {resultados[1]:.2f} Valor recebido: R$ {resultados[0]:.2f}")
