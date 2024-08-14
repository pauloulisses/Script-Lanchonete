print("Olá, seja bem-vindo à lanchonete do PAULO EBERSON ULISSES")

# Cria tabela com os produtos
tabela_produtos = {
    100: {"Descrição": "Cachorro-Quente", "Valor": 9.00},
    101: {"Descrição": "Cachorro-Quente Duplo", "Valor": 11.00},
    102: {"Descrição": "X-Egg", "Valor": 12.00},
    103: {"Descrição": "X-Salada", "Valor": 13.00},
    104: {"Descrição": "X-Bacon", "Valor": 14.00},
    105: {"Descrição": "X-Tudo", "Valor": 17.00},
    200: {"Descrição": "Refrigerante Lata", "Valor": 5.00},
    201: {"Descrição": "Chá Gelado", "Valor": 4.00}
}

# Imprime o cabeçalho do cardápio
print("****************** NOSSO MENU ******************")
print("| COD |           DESCRICAO            | VALOR |")

# Imprime cada item
for codigo, produto in tabela_produtos.items():
    descricao = produto["Descrição"]
    valor = produto["Valor"]
    print("| {:3d} | {:30s} | {:5.2f} |".format(codigo, descricao, valor))


total_pedido = 0

# while enquanto o usuário estiver informando opções
while True:
    codigo = int(input("Digite o código do produto desejado (ou digite 0 para encerrar): "))
    
    # Se o usuário digitar zero, utiliza-se o break para a execução do while
    if codigo == 0:
        break
    
    # Se o usuário digitar caractér inválido, utiliza-se o continue para continuar a execução do while
    if codigo not in tabela_produtos:
        print("Código inválido. Por favor, digite um código válido.")
        continue
    
    # Se tudo estiver OK, insere os dados
    produto = tabela_produtos[codigo]
    descricao = produto["Descrição"]
    valor = produto["Valor"]
    
    # Soma o total com os valores já adicionados
    total_pedido += valor
    print(f"Você pediu: {descricao}, no valor de: R$ {valor:.2f}")
    
    # Verifica se o usuário deseja pedir algo a mais, se a resposta for não, encerara o while
    resposta = input("Deseja pedir mais alguma coisa? (1- Sim | 0 - Não): ")
    if resposta == "0":
        break

print(f"O total a ser pago é: R$ {total_pedido:.2f}")
