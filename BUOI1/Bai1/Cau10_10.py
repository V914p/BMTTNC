def daoNguocChuoi(chuoi):
    return chuoi[::-1]
inputString = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là: ", daoNguocChuoi(inputString))