# primeiro exercicio de uma série de questões de construção de pequenos programas

#menu
print('Bem-vindo a loja do Zé do Caixão')

#variáveis




valor_do_produto = float(input('Entre com o valor do produto: '))
quantidade = float(input('Entre com a quantidade: '))
valor_final = valor_do_produto * quantidade
frete1 = 30
frete2 = 60
frete3 = 120
frete4 = 240

#PROGRAMA PRINCIPAL:

print('O valor sem frete foi: R${:.2f}'.format(valor_final))

if  quantidade < 11:
    print('O valor com frete foi: R${:.2f} (frete de R$30.00)'.format(valor_final + frete1))

elif quantidade < 101:
    print('O valor com frete foi: R${:.2f} (frete de R$60.00)'.format(valor_final + frete2))

elif quantidade < 1001:
    print('O valor com frete foi: R${:.2f} (frete de R$120.00)'.format(valor_final + frete3))

else:
    print('O valor com frete foi: R${:.2f} (frete de R$240.00)'.format(valor_final + frete4))








