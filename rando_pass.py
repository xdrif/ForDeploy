import random 
import string 

def genarate_key() -> None:
 while True:
  #########first section organized##################
  print('==================================')
  print(' Welcome To password genarator ')
  How_many= int(input('How many caractersin the password: '))
  Upper_case = str(input('Do you whant Upper case letter (y/n): ')).lower() == 'y'
  lower_case = str(input('letter lowecases (y/n)')).lower() == 'y'
  digit = str(input('Do u whant to add numbers (y/n)')).lower() == 'y'
  ################second section functionalities#####################
  characters = ''
  if Upper_case:
   characters += string.ascii_uppercase
  if lower_case:
   characters += string.ascii_lowercase
  if digit:
   characters += string.digits
   
  
  return ''.join(random.choice(characters)for _ in range(How_many) )



random_key = genarate_key()
print(f'Your key is {random_key}')
