
import hashlib

def calculate_sha256_hash(data):
    """
    Tính toán hàm băm SHA-256 của dữ liệu đầu vào bằng cách sử dụng mô-đun hashlib của Python.

    Args:
        data (str): Dữ liệu (chuỗi) để tính toán hàm băm.

    Returns:
        str: Hàm băm SHA-256 dưới dạng chuỗi thập lục phân.
    """
    # Tạo một đối tượng băm SHA-256
    sha256_hash = hashlib.sha256()

    # Cập nhật đối tượng băm với các byte của dữ liệu đầu vào.
    # Điều quan trọng là phải mã hóa chuỗi thành byte (ví dụ: 'utf-8') trước khi băm.
    sha256_hash.update(data.encode('utf-8'))

    # Trả về biểu diễn thập lục phân của hàm băm
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    # Nhắc người dùng nhập dữ liệu để băm bằng SHA-256
    data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")

    # Tính toán giá trị băm SHA-256 của dữ liệu đầu vào
    hash_value = calculate_sha256_hash(data_to_hash)

    # In dữ liệu gốc và giá trị băm SHA-256 của nó
    print(f"Giá trị hash SHA-256: {hash_value}")
