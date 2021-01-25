import random, time
num = int(input('Escolha um número entre 1 e 6: '))
dado = random.randint(1, 6)
print('Jogando o D...')
time.sleep(2)
print('Jogando o A...')
time.sleep(2)
print('Jogando o D...')
time.sleep(2)
print('Jogando o O...')
time.sleep(2)


if num == dado:
	print(f'Você escolheu {num} e caiu... {dado}')
	print('você ganhou!!')
elif num != dado:
	print(f'Você escolheu {num} e caiu... {dado}')
	print('você perdeu!!')

