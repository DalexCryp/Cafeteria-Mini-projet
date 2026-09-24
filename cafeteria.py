#Cafeteria Mini projet (DalexCryp)

def calcular_preco_unitario(bebida, tamanho):
    if bebida == "cafe":
        if tamanho == "P":
            return 4.00
        elif tamanho == "M":
            return 5.50
        else:
            return 7.00

    elif bebida == "capuccino":
        if tamanho == "P":
            return 6.00
        elif tamanho == "M":
            return 7.50
        else:
            return 9.00

    else:
        if tamanho == "P":
            return 5.50
        elif tamanho == "M":
            return 7.00
        else:
            return 8.50


def calcular_total(bebida, tamanho, quantidade, aluno_fiap):
    preco_unitario = calcular_preco_unitario(bebida, tamanho)
    valor_sem_desconto = preco_unitario * quantidade
    desconto = 0

    if aluno_fiap == "sim" and valor_sem_desconto > 15:
        desconto = valor_sem_desconto * 0.10

    valor_final = valor_sem_desconto - desconto
    return valor_sem_desconto, desconto, valor_final


def mostrar_resumo(nome, bebida, tamanho, quantidade, valor_sem_desconto, desconto, valor_final):
    print()
    print("--- RESUMO DO PEDIDO ---")
    print("Cliente:", nome)
    print("Pedido:", quantidade, bebida, "tamanho", tamanho)
    print("Valor sem desconto: R$", valor_sem_desconto)
    print("Desconto: R$", desconto)
    print("Valor final: R$", valor_final)

    if valor_final >= 20:
        print("Pedido com brinde!")
    else:
        print("Pedido sem brinde.")


nome = input("Digite o nome do cliente: ")
bebida = input("Digite a bebida (cafe, capuccino, chocolate): ")
tamanho = input("Digite o tamanho (P, M, G): ")
quantidade = int(input("Digite a quantidade: "))
aluno_fiap = input("É aluno FIAP? (sim ou nao): ")

valor_sem_desconto, desconto, valor_final = calcular_total(bebida, tamanho, quantidade, aluno_fiap)

mostrar_resumo(nome, bebida, tamanho, quantidade, valor_sem_desconto, desconto, valor_final)
