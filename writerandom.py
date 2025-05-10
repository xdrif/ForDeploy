import names
import csv
rand = names.get_first_name()

with open(f'{rand}.csv', mode='w' , encoding='utf-8') as file:
 writer  = csv.writer(file)

 writer.writerow(['name', 'gmail'])

 for i in range(100):

# Generate a random first name
  first_name = names.get_first_name()
  print(first_name)

# Generate a random last name
  last_name = names.get_last_name()
  print(last_name)

  full_name = f'{first_name} {last_name}'
  email = f'{first_name}{last_name}@gmail.com'

  writer.writerow([full_name , email])

  
  print(f'{rand}.csv'+ ' created sucsefully')
#trillion game