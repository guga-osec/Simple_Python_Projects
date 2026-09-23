
try:
	def padr(name):

		ip = input('IP: ').strip()
		name_server = input('Name server: ')
		fire = input('Firewall (Y/N): ')
		owname = input('Owner name: ')
		admin_name = input('Admin name: ')
		print('Acrescentações:')

		linhas = []
		while True:
			linha = input("\t")
			if linha == "":
				break
			linhas.append(linha)

		more = "\n\t".join(linhas)
		strings = f"""--------------------------------------
		\n\tColeta de Informação
		-> Site : {name}
		-> IP : {ip}
		-> Name Server : {name_server}
		-> Firewall (Y/n): {fire}
		-> Owner name: {owname}
		-> Admin name: {admin_name}

		Acrescentações (Enter vazio para sair):\n\t{more}"""

		with open(f"./informathion_gath_{name}.txt", "w" , encoding="utf-8") as f:
			f.write(strings)

	def wri(name):
		print()
		print('Type (Press Enter Without writing to leave):')
		linhas = [f'\nFootprint of: |   {name}   |']
		while True:
			linha = input("\t---> ")
			if linha == "":
				break
			linhas.append('---> '+linha)
		info = "\n\t\n".join(linhas)

		with open(f"./informathion_gath_{name}.txt", "w" , encoding="utf-8") as f:
			f.write(info)

	print()
	print( "-" * 5, "FootPrint_Saver", "-" * 5)
	options = ['Padrão', 'Write', 'Sair']

	while True:
		print('Opções:')
		for x in range(len(options)):
			print(f'\t{x} - {options[x]}')
		choose = int(input('>> ').strip())
		print()
		if choose != 2:
			name = input('Nome: ')
		if choose == 0:
			padr(name)
		elif choose == 1: 
			wri(name)
		elif choose == 2:
			exit()
		else:
			print('Erro X')

except:
	pass