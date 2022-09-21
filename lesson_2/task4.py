
print(' Введите первое число: ')
x = float(input())
print( ' Введите операцию: ')
s=input()
print( ' Введите второе число: ')
y = float(input())
if s == '+':
 print(x+y)
elif s == '-' :
 print(x-y)
elif s == '*':
 print(x*y)
elif s == '/':
 if y != 0:
  print(x/y)
 else :
    print(" Ошибка! На 0 делить нельзя")
else :
    print( "Ошибка")
                                      




