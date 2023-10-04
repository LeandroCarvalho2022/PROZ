for num in range(20, 0, -1): #iniciando em 20 para que faca a contagem decrescente.
    if num != 13: #utilizado != para que se o numero em questao for diferente ao numero 13 ele vai printar.
        print(num)

num = 20 #iniciando em 20 para que faca a contagem decrescente.
while num >= 1: #enquanto o numero for maior que 1
    if num != 13: #e diferente de 13, vai executar o comando, quando for 13 nao executara.
        print(num)
    num -= 1

#utilizei a funcao reversed : 'https://www.w3schools.com/python/ref_func_reversed.asp'
#range(1, 21) para criar uma sequência de 1 a 20, e em seguida, a função reversed inverte essa sequência, começando com 20 e indo até 1.
# O restante do código é o mesmo, verificando se o número atual não é igual a 13 e printando.
for num in reversed(range(1, 21)):
    if num != 13:
        print(num)
