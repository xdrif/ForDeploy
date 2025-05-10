from num2words import num2words


def num_converter():
    while True:
     try:
       """
      Conver any number to worlds"""
       i = int(input('enter a number: '))
       if i <0:
         print(f'the number is minus {num2words(abs(i))} , Is a negative number')
       elif i > 0:
        print(f'your number is  {num2words(i)} , a positive number')
       else:
        print(f'Your number is {i} ')
     except ValueError:
       print('Please enter a valid nuber')
    
num_converter()