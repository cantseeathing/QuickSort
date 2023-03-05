def swap(my_list, index1, index2):
    # temp = my_list[index1]
    # my_list[index1] = my_list[index2]
    # my_list[index2] = temp
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quickSort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quickSort(my_list, left, pivot_index - 1)
        quickSort(my_list, pivot_index + 1, right)
    return my_list


ex = [3, 5, 0, 6, 2, 1, 4]
# print(pivot(ex, 0, 6))
# print(ex)
print(quickSort(ex, 0, 6))
