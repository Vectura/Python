def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low < high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

mylist = [1, 4, 7, 8, 9, 10, 12, 14, 16, 18, 23]

print(binary_search(mylist, 12))