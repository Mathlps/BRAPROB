def exemplo_caso1():
    #1. Faça um Programa que leia uma lista de 5 números inteiros e mostre-os

    tamanho=int(input("Escreva o tamanho da sua lista(NÚMEROS INTEIROS):"))
    lista=[]

    for i in range(tamanho): #roda o programa de acordo com o tamanho da lista escolhida pelo usuario
        item = input(f"Digite o item {i + 1}: ")
        lista.append(item)  #adiciona itens a lista um de cada vez, podendo usar o .EXTEND para adicioar multiplos itens em uma unica vez
    print("Sua lista é:", lista)

def exemplo_caso2():
    # 2. Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa
    
    tamanho=int(input("Escreva o tamanho da sua lista(NÚMEROS INTEIROS):"))
    lista=[]

    for i in range(tamanho):
        item= input(f"Digite o {i + 1} numero: ")
        lista.append(item)
    
    lista.reverse() #inverte os elementos da lista
    print("Sua lista é (INVERTIDA):", lista)   

def exemplo_caso3():
    #3. Faça um Programa que leia uma lista de 4 notas, mostre as notas e a média na tela. 

    tamanho=int(input("Escreva o tamanho da sua lista(NÚMEROS INTEIROS):"))
    lista=[]

    for i in range(tamanho):
        item= int(input(f"Digite a {i+1} nota: "))
        lista.append(item)
    
    soma= sum(lista)
    media=soma/tamanho

    print(f"notas={lista} com a media total={media}")

def exemplo_caso4():
    #4. Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

    tamanho=int(input("Escreva o tamanho da sua lista(NÚMEROS INTEIROS):"))
    lista=[]

    for i in range(tamanho):
        item= input(f"Digite os caracteres {i+1}: ")
        lista.append(item)
    
    consoantes=[]
    vogais=['a','A','E','I','O','U','e','i','o','u']
    for caracter in lista:

        if caracter not in vogais:
            consoantes.append(caracter)

    print(f"\num total de {len(consoantes)} consoantes foram digitadas") #le a quantidade de itens que existem na lista
    print(f"\nas consoantes digitadas foram {consoantes} ")

def exemplo_caso5():
    #5. Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas. 

    tamanho=int(input("Escreva o tamanho da sua lista(NÚMEROS INTEIROS):"))
    lista=[]

    for i in range(tamanho):
        item= int(input(f"Digite os caracteres {i+1}: "))
        lista.append(item)
    
    pares=[]
    impares=[]

    for numeros in lista:
        if numeros % 2==0:
            pares.append(numeros)
        else:
            impares.append(numeros)

    print(f"\ntodos os números:{lista} \nnúmeros pares:{pares} \nnúmeros impares:{impares}")

def exemplo_caso6():
    #6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

    media_aluno=[]
    soma=0

    for i in range(10):
        print(f"\n Aluno {i+1}:")

        notas=[]
        for j in range(4):
            nota=float(input(f'\n Entre com a nota {j+1}:'))
            print(f'\n Nota {j+1}: {nota}')
            notas.append(nota)

            
        media=sum(notas)/4
        media_aluno.append(media)

        if media>=7:
            soma+=1
    
    print(f"\nTotal de Alunos com nota>=7 são:{ soma }")


def caso_padrao():
    
    print("Opção inválida. Este é o caso padrão.") # Código para o caso padrão quando nenhuma das opções é escolhida

def switch_case(opcao):
    opcoes = { # Mapeamento das opções para as funções dos exemplos
        1: exemplo_caso1,
        2: exemplo_caso2,
        3: exemplo_caso3,
        4: exemplo_caso4,
        5: exemplo_caso5,
        6: exemplo_caso6
    }
    return opcoes.get(opcao, caso_padrao)() # Chama a função correspondente ou redireciona para o caso padrão

opcao = int(input("Escolha uma opção (1 a 6): "))# Exemplo de uso:
switch_case(opcao)
