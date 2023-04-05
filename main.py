from os import system as s
class E(Exception):pass
class ItsNomalInOhio(E):pass
class CantEvenTypoIbOhio(E):pass
while 1:
	a=input('bruh need command : ')
	if a=='help':
		print('''help : help bruh by this command
trun off : bruh can turn off the Ohionux by Error (ScallSine)
Oshell : you can start you'r OS Terminal
f0Spy_hell : Ohionux Original Shell
''')
	elif a=='trun off':
		raise ItsNomalInOhio("Ok, I'll Shut Down...")
	elif a=='Oshell':
		print('exit by %quit%')
		s('python oshell.py')
	elif a=='f0Spy_hell':
		print('exit by $exit$')
		s('python f0spy_hell.py')
	else:
		raise CantEvenTypoIbOhio('you\'r wrong..... like that 1+1 is not 11.....')