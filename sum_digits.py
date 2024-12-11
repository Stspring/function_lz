
def sum_digits(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = input("Введите число(для которого вы хотите найти сумму цифр")
S = sum_digits(n)
print("Сумма цифр в числе", n ,"равна", S)







