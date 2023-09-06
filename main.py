year= int(input('Enter the year:'))
if(year%4==0)and(year%100!=0):
  print(f'The given year{year} is leap year')
else:
  print(f'The given year{year}is not a leap year')