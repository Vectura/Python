
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)  

# print(fact(6))


def summArr(x, n):
    if n == 0:
        return 0
    return x[n-1] + summArr(x, n-1)

n = int(input("Enter lenght arr: "))
m = []
for i in range(0, n):
    item = int(input("Enter item arr: "))
    m.append(item)
print(m)
print("Cумма элементов массива равна: ", summArr(m, n))