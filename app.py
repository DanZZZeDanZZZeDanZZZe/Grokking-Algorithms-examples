from binary_search import binary_search as bs
from quick_sort import  quick_sort as qs
num_list = [1, 2, 4, 6, 5, 6, 7]
arr = [1, 4, 7, 3, 5, 6, 3]
print(bs.binary_search(num_list, 4))
print(bs.binary_search(num_list, 9))

print(qs.quicksort(arr))