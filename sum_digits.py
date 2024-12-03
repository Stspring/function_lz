
def sum_digits(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = input("Введите число")
print(sum_digits(n))