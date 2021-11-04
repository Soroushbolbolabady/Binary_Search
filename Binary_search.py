
number = int(input("Enter number : "))

array = []
for i in range(1,100):
	array.append(i)





def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)



print("Searching for {}".format(number))
print("Index of {}: {}".format(number, binary_search_recursive(array, number, 0, len(array))))