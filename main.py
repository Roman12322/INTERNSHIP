"""
1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному
по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.
"""

import time
import random


def isEven(val):
    try:
        if val % 2 == 0:
            print(f"Value '{val}' is even")
            return True
        else:
            print(f"Value '{val}' is not even")
            return False

    except:
        print("Incorrect type")


start_time = time.time()
a = isEven(4.0)
b = isEven(3.2)
print(f"Время выполнения {time.time() - start_time}")


def isEven_2ndVariation(val):
    try:
        if val & 1:
            print(f"Value '{val}' is not even")
            return False
        else:
            print(f"Value '{val}' is  even")
            return True

    except:
        print("Incorrect type")
        return 0


start_time_1 = time.time()
isEven_2ndVariation(1)
isEven_2ndVariation(2)
print(f"Время выполнения {time.time() - start_time_1}")

"""
2. На языке Python (2.7) реализовать минимум 
по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
"""


class First:
    def __init__(self):
        self.QUEUE = []
        print("Очередь создана")

    def pop(self):
        try:
            return self.QUEUE.pop(0)
        except:
            print('Unable to delete item')

    def add_item(self, value):
        try:
            return self.QUEUE.insert(0, value)
        except:
            print("Unable to add item")

    def show_FIFO_SYS(self):
        print(self.QUEUE)

class Node:
    def __init__(self, value):
        self.value = value

class Second:
    def __init__(self):
        self.QUEUE = []
        print("Очередь создана")

    def pop(self):
        try:
            return self.QUEUE.pop(0)
        except:
            print('Unable to delete item')

    def add_item(self, value):
        try:
            new_item = Node(value)
            return self.QUEUE.insert(0, new_item)
        except:
            print("Unable to add item")

    def show_FIFO_SYS(self):
        print(self.QUEUE)

fifo_1 = First()
fifo_1.pop()
fifo_1.add_item(13)
fifo_1.add_item(12)
fifo_1.show_FIFO_SYS()
fifo_1.pop()
fifo_1.show_FIFO_SYS()

fifo_2 = First()
fifo_2.pop()
fifo_2.add_item(3)
fifo_2.add_item(2)
fifo_2.show_FIFO_SYS()
fifo_2.pop()
fifo_2.show_FIFO_SYS()

"""
3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. 
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
 Объяснить почему вы считаете, что функция соответствует заданным критериям.
"""
def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        q = random.choice(list)
    l_nums = [n for n in list if n < q]

    e_nums = [q] * list.count(q)
    b_nums = [n for n in list if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)

my_list = [random.randint(0, 432) for i in range(10000)]
mylist = quicksort(my_list)
print(mylist)


