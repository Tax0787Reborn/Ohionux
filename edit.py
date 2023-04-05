try:
	print("BZ3's OhioTaxNux Editer is just open")
	with open(input('file : '),input('mode : ')) as f:
		a=''
		while 1:
			a=input(': >[ BZ3 ]> ')
			if a!='%quit%':
				b=eval('f.'+a)
				print(b)
			else:
				break
	print("BZ3's OhioNux Editer is closed")
except Exception as error:
	print('ERROR')
	print('type :',type(error),'what? :',error)
