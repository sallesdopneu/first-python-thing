import sys
import re

email = input('insira seu e-mail ')

email.lower()

while email:
    if "@" and ".com"  in email and len(email) >= 6:
        break
    else:
        email = print('\ninsira um email válido', file=sys.stderr)
        email = input('\nTente novamente ')

senha = input('Insira uma senha (deve conter pelo menos 8 dígitos, letras maiúsculas e minúsculas e numeros) ')

while senha:
    if any(c.isupper() for c in senha) and any(c.islower()for c in senha)\
    and len(senha) >=8 and any(c.isdigit() for c in senha):

        break
    else:
        print('\nEsta senha é invalida' , file=sys.stderr)
        senha = input('\nTente novamente ')

print(email)
print(senha)


# print(email.py)