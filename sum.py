
# создаю функцию sum_L(она принемает значение а)
# а строка в которую будут передаваться числа
def sum_L(a):
    b = a.split()        # разбиваем строку а на части по пробелам
    c = 0                # ввожу переменную c(в нее будет сохраняться сумма чисел из списка)           
    for i in range(0,len(b)):       # использую цикл для подсчета суммы
        c = c + int(b[i])           # b[i] элемент списка в виде(str), который преобразуется в int
    return(c)                   # после завершения цикла возвращается итоговая сумма


list = input("Введите список из чисел ")       # пользователь вводит числа(с пробелами) которые сохраняются в list
sum_vs = sum_L(list)                # вызывется функция sum_L.
print("Сумма всех чисел в списке равна", sum_vs)   # выводится сумма чисел в списке


