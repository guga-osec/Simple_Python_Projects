import argparse
import dns.resolver

def resolver(hostname):
	try:
		res = dns.resolver.resolve(hostname, "A")
		for ips in res:
			print(f"[+] {hostname} -> {ips}\n")

	except (dns.resolver.NXDOMAIN,dns.resolver.NoAnswer,dns.resolver.Timeout):
		print(f'--> No subdomains found <--\n')


def main():
	parser = argparse.ArgumentParser(description="DNS resolver")
	parser.add_argument("-d","--domain", required=True,help='target domain')
	parser.add_argument("-w","--worldlist", required=False,help="worldlist")
	parser.add_argument("-s","--singlewords", nargs='+', required=False, help="manually subdomain")
	args = parser.parse_args()
	
	print("\nDomain:  ",args.domain)
	if args.worldlist:
		print("\nWorldlist: ", args.worldlist)
		with open(args.worldlist, "r", encoding="utf-8") as f:
			for word in f:
				word = word.strip()
				if not word:
					continue
				hostname = f"{word}.{args.domain}"
				resolver(hostname)
	if args.singlewords:
		print('Subdomains: ', args.singlewords)
		print()
		for word in args.singlewords:
			hostname= f"{word}.{args.domain}"
			resolver(hostname)
if __name__ == "__main__":
	main()
