import base64

def main():
    input_string = input("NhậP thông tin cần mã hoá: ")

    encode_bytes = base64.b64encode(input_string.encode("utf-8"))
    encode_string = encode_bytes.decode("utf-8")

    with open("data.txt", "w") as file:
        file.write(encode_string)

    print("Đã mã hoá và ghi vào tệp data.txt")

if __name__ == "__main__":
    main()
