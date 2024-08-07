cpf_dig=[]


def pridigito(cpf_dig):
    cont1=10
    soma=dv1=0
    for k in cpf_dig:
        prod = cont1 * k
        soma += prod
        cont1 -= 1
        if cont1 < 2:
            break
    dv1 = 11 - (soma % 11)
    if dv1 > 9:
        dv1 = 0
    return dv1


def segdigito(cpf_dig):
    cont2=11
    soma=0
    for k in cpf_dig:
        prod2 = cont2 * k
        soma += prod2
        cont2 -= 1
        if cont2 < 2:
            break
    dv2 = 11 - (soma % 11)
    if dv2 > 9:
        dv2 = 0
    return dv2


def validacpf(cpf_dig):
    r1= pridigito(cpf_dig)
    r2= segdigito(cpf_dig)
    if cpf_dig[9] == r1 and cpf_dig[10] == r2:
        return 'CPF VALIDO!'
    else:
        return 'CPF INVALIDO!'


cpf=''
while len(cpf) !=11 or cpf.isalpha():
    cpf = input('Informe o cpf (11digitos): ').strip()
for v in cpf:
    cpf_dig.append(int(v))
print(validacpf(cpf_dig))
#66755631736