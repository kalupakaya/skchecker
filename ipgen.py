import random
import requests
import os
from multiprocessing.dummy import Pool
from faker import Faker  


def genip():

	brapa = input('How Much IP? ')
	for i in range(0, int(brapa)):
		faker = Faker()  
		ip_address = faker.ipv4() 
		print('RANDOM IP ->', ip_address)
		open('ip.txt', 'a').write(ip_address+'\n')
	print('[+] SUCCESS GENERATE IP!! ')

def yoy():

	lis = input('Your IP List -> ')
	tol = open(lis, 'r').readlines()
	for i in tol:
		yaa = i.strip()
		part = yaa.split('.')
		a = '.'

		start = 0
		end = 244
		for j in range(start, end + 1):
			for k in range(start, end + 1):
				ale = part[0] + a + part[1] + a + str(j) + a + str(k)
				open('rang.txt', 'a').write(ale+'\n')
		print(yaa, '-> RANGED!!')


def valid(hayuk):

		try:
			r = requests.get('http://{}'.format(hayuk), timeout=3)
			if r.status_code == 200:
				print(hayuk, '-> LIVE IP')
				open('liveip.txt', 'a').write(hayuk+'\n')
			elif '<title>' in r.text:
				print(hayuk, '-> LIVE IP')
				open('liveip.txt', 'a').write(hayuk+'\n')
			else:
				pass
		except Exception:
			print(hayuk, '-> DEAD')




def thread(li):
	ase = open(li, 'r').read().splitlines()
	p = Pool(500)
	p.map(valid, ase)

if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""



                            \033[91m███╗░░██╗███████╗██╗░░░██╗███████╗██████╗░  ██████╗░░█████╗░░█████╗░██╗░░██╗
                            \033[92m████╗░██║██╔════╝██║░░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
                            \033[93m██╔██╗██║█████╗░░╚██╗░██╔╝█████╗░░██████╔╝  ██████╦╝███████║██║░░╚═╝█████═╝░
                            \033[94m██║╚████║██╔══╝░░░╚████╔╝░██╔══╝░░██╔══██╗  ██╔══██╗██╔══██║██║░░██╗██╔═██╗░
                            \033[95m██║░╚███║███████╗░░╚██╔╝░░███████╗██║░░██║  ██████╦╝██║░░██║╚█████╔╝██║░╚██╗
                            \033[96m╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

  Author : NeverBack
  Attack Cyber                    

		"""+'\n')

	print('(+) \033[95m(1). GENERATE IP')
	print('(+) \033[93m(2). RANGE IP')
	print('(+) \033[92m(3). IP CHECKER'+'\n')

	pilih = input('\033[91m Select Options -> ')

	if pilih == '1':
		genip()
	elif pilih == '2':
		yoy()
	elif pilih == '3':
		diem = input('Input Your IP LIST -> ')
		thread(diem)
	else:
		print('No Options!')

