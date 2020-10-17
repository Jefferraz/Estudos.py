"""
nome = input('Qual é o seu nome?')
idade = input('Qual é a sua idade?')
peso = input('Qual é o seu peso?')

print(nome, idade, peso)
"""

"""
nome = input("Qual é o seu nome?")
print('Ola ' + nome + '! Prazer em te conhecer!')
"""

"""
dia = input('Dia:')
mes = input('Mes:')
ano = input('Ano:')

print('Você nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano + '. Correto?')
"""

"""
#Atribuição de tipo primitivo para realizar operações matamáticas;
#Sintaxe do print; 

soma1 = int(input('Digite o primeito nunmero:'))
soma2 = int(input('Digite o segundo numero:'))

soma = soma1 + soma2

print('A soma entre {} e {} vale {}'.format(soma1, soma2, soma))
"""

"""
#Consultando tipagem de variáveis;

info = input('Digite uma informação:')
print(type(info))
print(info.isalnum())
print(info.isalpha())
print(info.isdecimal())
print(info.islower())
"""

""""
#Programa para calcular média;

nome = input('Digite o nome do aluno:')

n1 = float(input('Digite a nota do primeiro bimestre:'))

n2 = float(input('Digite a nota do segundo bimestre:'))

n3 = float(input('Digite a nota do terceiro bimestre:'))

n4 = float(input('Digite a nota do quarto bimestre:'))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print('As notas obtidas pelo aluno:', nome,
          'foram: {} # {} # {} # {}. E sua média é: {}'.format(n1, n2, n3, n4, media))
    print('Parabéns, você foi aprovado!')
else:
    print('As notas obtidas pelo aluno:', nome,
          'foram: {} # {} # {} # {}. E sua média é: {}'.format(n1, n2, n3, n4, media))
    print('Você foi reprovado, estude mais!')
"""

"""
Upando no Git:

Add: Ctrl + Alt + A
Commit: Ctrl + K
Push: Ctrl + Shift + K
"""

"""
# Faça um programa que leia um número inteiro e mostra na tela seu sucessor e seu antecessor

numero = int(input('Digite um número:'))

numero += 1

print(numero)

numero -= 2

print(numero)
"""

"""
# Crie um algoritmo que leia um número e mostre o seu dobro, triple e raiz quadrada

numero = int(input('Digite um número:'))

mult2 = numero * 2

mult3 = numero * 3

raiz = numero ** (1 / 2)

print('O número multiplicado por 2 é: {}, multiplicado por 3 é: {} e a raiz quadrada é {}'.format(mult2, mult3, raiz))
"""

"""
#Desenvolvia um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = (nota1 + nota2) / 2

print('A média do aluno é: {}'.format(media))
"""

"""
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite o valor em metros desejado:'))

centimetros = metros * 100

milimetros = metros * 1000

print('O valor digitado em metros convertido para centímetros é: {}cm. E para milímetros: {}mm'.format(centimetros, milimetros))
"""

"""
#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Digite um número:'))

print(numero * 1)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
"""

"""
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

valor = float(input('Digite o valor em reais que você possúi:'))

valor = valor / 3.27

print('Com esse valor em reais, você pode comprar: {0:.1f} dolares'.format(valor))
"""

"""
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m

largura = float(input('Digite a Largura da parede em metros:'))
altura = float(input('Digite a altura da parede em metros:'))

area = largura * altura

tinta = 2

litros = area / tinta

print('A quantidade de tinta em litros necessária para pintar essa parede é: {}l'.format(litros))
"""

"""
#Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto

preço = float(input('Digite o preço do produto:'))

desconto = preço - (preço / 100) * 5

print('O valor do produto com desconto de 5% aplicados é: {}'.format(desconto))
"""

"""
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Com 15% de aumento

salario = float(input('Digite o seu salário:'))

aumento = (salario / 100) * 15 + salario

print('O novo salário com 15% de aumento é: {}'.format(aumento))
"""