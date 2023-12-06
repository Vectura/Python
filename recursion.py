# факториал числа
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)  

# print(fact(6))

# Сумма элементов массива
# def summArr(x, n):
#     if n == 0:
#         return 0
#     return x[n-1] + summArr(x, n-1)

# Поиск максимального значения 
# def Search(x, n):
#     if n == 1:
#         return x[0]
#     elif x[0] <= x[n-1]:
#          x[0] = x[n-1]
#          return Search(x[0:-1], n-1)
#     elif x[0] >= x[n-1]:
#          return Search(x[0:-1], n-1)
    
def multiTable(x, n):
    if n == 1:
        total = x[0] * 2
        print(total)
    elif n > 0:
        total = x[0] * x[n-1]
        print(total)
        return multiTable(x[0:-1], n-1)

n = int(input("Enter lenght list: "))
m = []
for i in range(0, n):
    item = int(input("Enter item list: "))
    m.append(item)
print(m) 
multiTable(m, n)


