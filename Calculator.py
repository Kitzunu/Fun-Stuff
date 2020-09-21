x = float(input("Enter your 1st number: "))
y = float(input("Enter your 2nd number: "))
add = str(x+y)
sub = str(x-y)
mult = str(x*y)
if y == 0:
    div = "ERROR! Dividing by 0 is undefined!"
else:
    div = str(x/y)

print('{} / {} = '.format(x, y) + div  + '\n' +
      '{} * {} = '.format(x, y) + mult + '\n' +
      '{} + {} = '.format(x, y) + add  + '\n' +
      '{} - {} = '.format(x, y) + sub)
