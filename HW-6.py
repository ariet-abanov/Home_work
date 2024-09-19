def bubble_sort(buble_sort_list):
    n = len(bubble_sort_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if bubble_sort_list[j] > bubble_sort_list[j + 1]:
                bubble_sort_list[j], bubble_sort_list[j + 1] = bubble_sort_list[j + 1], bubble_sort_list[j]
    return bubble_sort_list

bubble_sort_list = [1, 7, 4, 9, 3, 6]

print_buble = bubble_sort(bubble_sort_list)
print(print_buble)

def binary_search(a, value):
    n = len(a)
    first = 0
    last = n - 1
    middle = n // 2
    resultOk = False
    while a[middle] != value and first <= last:
        if value > a[middle]:
            first = middle + 1
        else:
            last = middle - 1
        middle = (first + last) // 2
    if value == a[middle]:
        resultOk = True

    if resultOk == True:
        print(f'ID of value {value} == {middle}')
    else:
        print('No value')
lst = [12, 34, 7, 10, 3, 6, 37]
print(lst)
binary_search(lst, 37)
binary_search(lst, 12)