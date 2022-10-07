# Задача 4.	Реализуйте алгоритм перемешивания списка, без использования 
# встроенных методов (особенно SHUFFLE, без него). Можно (нужно) использовать библиотеку Random.
import random
list1=['1', 'Погода', '2', 'Good', '3', '***', '4', '5']
print('Исходный список: ' + str(list1))
for i in range (len(list1)-1):
    j=random.randint(0, len(list1)-1)
    list1[i], list1[j] = list1[j], list1[i]
print('Перемешанный список: ' + str(list1))
