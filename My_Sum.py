from tkinter import N

def my_sum(*args):
    print(args)
    print(type(args))
    sum = 0
    for i in args:
        sum += i
    return sum

# args = input("please enter the number which you want to sum\n")
# print(my_sum(args))
'''
因為透過input輸入的值會只有tuple(0)且式str,後面則是null
('1 2 3',)
'''

print(my_sum(1,2,3))