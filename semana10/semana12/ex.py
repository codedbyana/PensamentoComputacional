#Crie um algoritmo que simule o sistema de pedidos de uma lanchonete. O programa deve exibir o seguinte menu principal:
#===== LANCHONETE BYTEBURG =====
#1 - Fazer pedido
#2 - Cancelar pedido
#3 - Mostrar cardápio
#4 - Mostrar total do pedido
#5 - Confirmar compra
#6 - Sair
#===============================
#O cliente só pode ter um pedido ativo por vez.
#O sistema deve permitir adicionar um único item por vez, substituir o pedido atual ou cancelar completamente antes da confirmação.
#Regras do sistema
#O pedido inicial é vazio e o total é igual a R$ 0,00.
#Cada item do cardápio possui um código fixo e um valor:
#1 - X-Salada ........ R$ 10,00
#2 - X-Bacon ......... R$ 12,00
#3 - Refrigerante .... R$ 5,00
#4 - Suco natural .... R$ 6,00
#5 - Batata frita .... R$ 7,00
#O sistema deve mostrar o cardápio sempre que o usuário desejar.
#O cliente pode:
#Fazer um novo pedido (substitui o anterior);
#Cancelar o pedido atual (zera o total);
#Visualizar o total do pedido atual;
#Confirmar a compra, mostrando o valor final e uma mensagem de agradecimento.


def mostrar_cardapio():
    print("===== CARDÁPIO =====")
    print("1 - X-Salada ........ R$ 10,00")
    print("2 - X-Bacon ......... R$ 12,00")
    print("3 - Refrigerante .... R$ 5,00")
    print("4 - Suco natural .... R$ 6,00")
    print("5 - Batata frita .... R$ 7,00")
    print("=====================")

def fazer_pedido():
    mostrar_cardapio()
    codigo = int(input("Digite o código do item desejado: "))

    precos = {
        1: ("X-Salada", 10.00),
        2: ("X-Bacon", 12.00),
        3: ("Refrigerante", 5.00),
        4: ("Suco natural", 6.00),
        5: ("Batata frita", 7.00)
    }

    if codigo in precos:
        item, valor = precos[codigo]
        print(f"Você pediu {item} - R$ {valor:.2f}")
        return item, valor
    else:
        print("Código inválido!")
        return None, 0

# Programa principal
pedido = None
total = 0.0

while True:
    print("\n===== LANCHONETE BYTEBURG =====")
    print("1 - Fazer pedido")
    print("2 - Cancelar pedido")
    print("3 - Mostrar cardápio")
    print("4 - Mostrar total do pedido")
    print("5 - Confirmar compra")
    print("6 - Sair")
    print("===============================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pedido, total = fazer_pedido()

    elif opcao == "2":
        pedido = None
        total = 0.0
        print("Pedido cancelado com sucesso!")

    elif opcao == "3":
        mostrar_cardapio()

    elif opcao == "4":
        if pedido:
            print(f"Pedido atual: {pedido} - Total: R$ {total:.2f}")
        else:
            print("Nenhum pedido ativo no momento.")

    elif opcao == "5":
        if pedido:
            print(f"Compra confirmada! Total: R$ {total:.2f}")
            print("Obrigado pela preferência! ")
            pedido = None
            total = 0.0
        else:
            print("Você não tem nenhum pedido para confirmar.")

    elif opcao == "6":
        print("Encerrando o sistema... Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")
