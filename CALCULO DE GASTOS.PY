valor_gasto=[50,34,2,1]
valor_recebido=[90,30,10,3]

def listar(valor_gasto,valor_recebido):
    total_gasto, total_entrada = float(sum(valor_gasto)),float(sum(valor_recebido))
    saldo = total_entrada-total_gasto
    print(f"O saldo total da conta é R$ {saldo:.2f} Valor gasto: R$ {total_gasto:.2f} Valor recebido: R$ {total_entrada:.2f}")
    return total_entrada,total_gasto,saldo
while True:
    option = input('tipo de consulta\n1-saldo \n2-entradas \n3-gastos\n0-sair')
    consulta ={"1":"saldo","2":"entrada","3":"gasto","0":"sair"} 
    

    listar(valor_gasto,valor_recebido)
