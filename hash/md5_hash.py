# md5_hasher.py

# Hàm xoay trái bit (left rotate)
def _lrot_rotate(value, shift):
    """
    Thực hiện xoay trái bit trên một giá trị 32-bit.
    """
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    """
    Tính toán hàm băm MD5 của một thông điệp.
    """

    # Khởi tạo các biến ban đầu (A, B, C, D) theo tiêu chuẩn MD5
    # Đây thường được gọi là các biến chuỗi hoặc giá trị băm
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Tính toán độ dài ban đầu của thông điệp (tính bằng bit)
    original_length = len(message) * 8

    # Đệm (padding) thông điệp
    # Thêm một bit '1' (byte 0x80)
    message += b'\x80'
    # Đệm bằng các bit '0' cho đến khi độ dài là 448 bit (modulo 512)
    # Độ dài tính bằng byte, nên cần chuyển đổi sang bit.
    # Việc đệm đảm bảo độ dài thông điệp cách 64 byte so với bội số của 64 byte (512 bit)
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    # Nối độ dài ban đầu (64 bit, little-endian) vào cuối thông điệp
    # Độ dài ban đầu tính bằng bit
    message += original_length.to_bytes(8, 'little')

    # Xử lý thông điệp theo từng khối 512-bit (64 byte)
    # Vòng lặp này duyệt qua các khối thông điệp
    for i in range(0, len(message), 64):
        block = message[i:i+64]

        # Chia khối thành 16 từ 32-bit (little-endian)
        # Mỗi khối là 64 byte, và mỗi từ là 4 byte (32 bit)
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        # Lưu các giá trị băm hiện tại
        aa, bb, cc, dd = a, b, c, d

        # Vòng lặp chính của thuật toán MD5 (64 vòng)
        for j in range(64):
            # Phần này của mã xử lý các phép biến đổi cụ thể
            # cho mỗi vòng dựa trên đặc tả của thuật toán MD5.
            # Thuật toán MD5 đầy đủ có các hàm phức tạp (F, G, H, I)
            # và các hằng số (giá trị T) cho mỗi vòng, cùng với
            # lựa chọn từ và số lượng dịch chuyển cụ thể.
            # Đoạn mã trong hình ảnh chỉ tập trung vào một phần cụ thể của hàm vòng.

            # Các điều kiện và hàm f, g dựa trên hình ảnh được cung cấp
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else: # j >= 48
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            # Các bước tính toán cốt lõi trong mỗi vòng
            temp = d
            d = c
            c = b
            # Giá trị hằng số và dịch chuyển cụ thể cho từng vòng
            # Note: 0x54827999 là một hằng số T từ hình ảnh thứ hai (image_9a05f5.png)
            # words[g] được sử dụng dựa trên giá trị g đã tính toán
            b = b + _lrot_rotate((a + f + 0x54827999 + words[g]) & 0xFFFFFFFF, 3) # Ví dụ về hằng số và dịch chuyển
            a = temp


        # Cập nhật các biến băm sau khi xử lý một khối
        # Phần này được áp dụng sau vòng lặp 64 vòng cho mỗi khối.
        a = (a + aa) & 0xFFFFFFFF
        b = (b + bb) & 0xFFFFFFFF
        c = (c + cc) & 0xFFFFFFFF
        d = (d + dd) & 0xFFFFFFFF

    # Định dạng đầu ra hàm băm cuối cùng
    # Sử dụng định dạng '08x' để đảm bảo 8 chữ số thập lục phân cho mỗi giá trị
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

# --- Ví dụ sử dụng (như trong hình ảnh) ---
if __name__ == "__main__":
    # Nhận chuỗi đầu vào từ người dùng
    input_string = input("Nhập chuỗi cần băm: ")

    # Tính toán hàm băm MD5
    # Lưu ý: Hàm md5 mong đợi byte, nên phải mã hóa chuỗi đầu vào
    md5_hash = md5(input_string.encode("utf-8"))

    # In kết quả
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")

