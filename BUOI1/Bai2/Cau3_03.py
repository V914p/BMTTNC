def taoTupleTuList(lst):
    return tuple(lst)
inputList = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inputList.split(',')))

myTuple = taoTupleTuList(numbers)
print("List: ", numbers)
print("Tuple từ List: ", myTuple)