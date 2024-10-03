# Você está organizando um churrasco e precisa gerenciar a lista de convidados. Crie um programa em Python que:

    # Solicite ao usuário que insira o nome de até 7 convidados.
    # Armazene os nomes em uma lista.
    # Permita ao usuário remover um convidado da lista, caso necessário.
    # Exiba a lista final de convidados.

    # Digite o nome do convidado 1: João
    # Digite o nome do convidado 2: Maria
    # ...
    # Digite o nome do convidado 7: Pedro
    # Deseja remover algum convidado da lista? (sim/não): sim
    # Digite o nome do convidado a ser removido: Maria

# Lista para armazenar os nomes dos convidados
listaChurras = []

# Solicitar o nome de até 7 convidados
for i in range(1, 8):
    nome = input(f"Digite o nome do convidado {i}: ")
    listaChurras.append(nome)

# Exibir a lista de convidados
print("\nLista de convidados:")
for convidado in listaChurras:
    print(convidado)
