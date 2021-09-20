#cia = '\033[1;36m'
cl = '\033[0m'
az = '\033[1;94m'
cia = '\033[1;36m'
cz = '\033[1;37m'

import requests
import os
from sys import argv, executable
import base64


def restart():
    os.execl(executable, executable, *argv)

def Enter():
    input("Pressione ENTER para continuar")
    
    restart()

def clear():
    os.system('cls||clear')
    

def opcoes():
    print('{}MILICIA PIKA DE MEL\033[0m'.format(cia))
    print(' ')
    print('\033[4;37mCRIADO POR: SWAG,MRDINIZ,SPYWARE,INTACTOX\033[0;0m')
    print('\033[4;37mGITHUB: Swag666baby // Spyware0 // mrdiniz88\033[m')
    print('ZAP: 556295598220')
    print(' ')
    print('ESCOLHA UM NÚMERO: ')
    print(' ')
    print('{}[{}1{}]{} CONSULTA DE CEP'.format(cl,cia,cl,cia))
    print('{}[{}2{}]{} CONSULTA DE IP'.format(cl,cia,cl,cia))
    print('{}[{}3{}]{} CONSULTA DE CNPJ'.format(cl,cia,cl,cia))
    print('{}[{}4{}]{} CONSULTA DE PLACA'.format(cl,cia,cl,cia))
    opc = input('>>>  {}'.format(cl))

    if opc == '1':
    	Cep()

    elif opc == '2':
    	Ip()

    elif opc == '3':
    	Cnpj()
    	
    elif opc == '4':
    	placa()
    	
    else:
        restart()


def Ip():
    clear()

    ip = input('DIGITE O IP: ')
 
    r = requests.get(f'https://ipwhois.app/json/{ip}')
    data = r.json()
    clear()
    for item in data:
        print(item,':', data[item])
    Enter()


def Cep():
    clear()

    cep = input('DIGITE O CEP: ')
    a = requests.get(f'https://viacep.com.br/ws/{cep}/json')
    cp = a.json()
    clear()
    for item in cp:
        print(item,':', cp[item])
    Enter()

def Cnpj():
    clear()
    cnpj = input('DIGITE O CNPJ: ')
	
    b = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
	
    pj = b.json()
    
    clear()
	
    for item in pj:
        print(item,':', pj[item])
    Enter()

def placa():
    clear()
    placa = input('DIGITE A PLACA: ')
	
    u = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False)
	
    pj = u.json()
    
    clear()
    for item in pj:
        print(item,':', pj[item])
    Enter()

clear()

opcoes()
