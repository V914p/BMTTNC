def demSoLanXuatHien(lst):
    countDict = {}
    for item in lst:
        if item in countDict:
            countDict[item] +=1
        else:
            countDict[item] = 1
    return countDict

inputString = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
worldList = inputString.split()

soLanXuatHien = demSoLanXuatHien(worldList)
print("Số lần xuất hiện của các phần từ : ",soLanXuatHien)