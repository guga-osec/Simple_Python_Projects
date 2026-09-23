import socket
from colorama import Fore, init

init()
try:
	choice = int(input('\n--> Port Scan tool\n\t0 - verify connection\n\t1 - Send message\n\t2 - search open ports\n>> '))

	ports = [20,21,22,80,443,8080,445, 3306, 25, 53, 3389,993, 995]

	def verify_port(domain_or_ip,port, seec='y'):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM)	as cli:
			client.settimeout(0.2)
			code = client.connect_ex((domain_or_ip, port))

		open_ports = []
		closed_ports = []

		if code == 0:
			open_ports.append(Fore.GREEN + f'port {port} : [O] open - {code}' + Fore.RESET )
		else:
			closed_ports.append(Fore.RED + f'port {port} : [X] closed - {code}' + Fore.RESET)

		for ro in range(len(open_ports)):
			print(f'\t{open_ports[ro]}')
		if seec == 'y' and len(closed_ports) > 0:
			for rc in range(len(closed_ports)):
				print(f'\t{closed_ports[rc]}')
		
	def blue_text(text):
		text = Fore.BLUE + text + Fore.RESET
		return text

	def search_ports(ports):
		c = input(blue_text('\nSee closed doors(y/N): ')).lower()
		print('\n-> Starting the scan...')
		for port in ports:
			verify_port(domain_or_ip,port=port,seec=c)

	def send_message(host, port):
		message = input(blue_text("Message: "))

		try:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
				client.settimeout(2)
				client.connect((host, port))
				client.sendall(message.encode())

				try:
					response = client.recv(1024)
					print("\nResposta:")
					print(response.decode(errors="replace"))
				except socket.timeout:
					print("\nThe server didn't reply.")

		except Exception as e:
			print(Fore.RED + f"\nError: {e}")

	domain_or_ip = input(blue_text( 'Domain/IP: '))
	port = int(input(blue_text('PORT: ')))

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.5)

	if choice == 0:
		verify_port(domain_or_ip,port=port, seec='y')

	elif choice == 1:
		send_message(domain_or_ip,port)

	elif choice == 2:
		ddq = input(blue_text('Wanna choose the doors (y/N): ')).upper()
		if ddq == 'Y':
			portas = input(blue_text('Enter the doors (split them with "," ): ')).strip()
			if ',' in portas:
				portas = portas.split(',')
				ports.clear()
				for p in portas:
					ports.append(int(p))
				search_ports(ports)
		elif ddq == 'N' or ddq == '':
			search_ports(ports)
		else: 
			print('Invalid Choice')
except:
	pass
print()

