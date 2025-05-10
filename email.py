email = str(input('Plase enter your email: ')).strip()
if '@' in email:
    username = email [:email.index('@')]
    domain = email [email.index('@') +1:]
    print('##########################################')
    print(f'Usename={username} \nDomain={domain}')
    print('##########################################')
else:
    print('invalid mail adress')
