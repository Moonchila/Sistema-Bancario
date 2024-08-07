import re

regex= r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def checkemail(email):
    if re.fullmatch(regex, email):
        print('E-mail Valido')
    else:
        print('E-mail Invalido')

ler=input('Informe seu e-mail: ')
checkemail(ler)