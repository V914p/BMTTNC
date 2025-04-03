class TranspositionCipher:
    def __init__(self):  # Hàm khởi tạo
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):  # Duyệt qua từng cột
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]  # Thêm ký tự theo cột
                pointer += key  # Di chuyển theo bước nhảy (step)
        return encrypted_text
    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row, col = 0, 0
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            if col == key or (col == key - 1 and row == len(text) % key):
                col = 0
                row += 1
        return ''.join(decrypted_text)
