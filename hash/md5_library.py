
import hashlib

def calculate_md5(input_string):
    """
    Calculates the MD5 hash of the given input string using Python's hashlib module.

    Args:
        input_string (str): The string for which to calculate the MD5 hash.

    Returns:
        str: The MD5 hash as a hexadecimal string.
    """
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the input string.
    # It's crucial to encode the string to bytes (e.g., 'utf-8') before hashing.
    md5_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    return md5_hash.hexdigest()

if __name__ == "__main__":
    # Prompt the user to enter a string
    input_string = input("Nhập chuỗi cần băm: ")

    # Calculate the MD5 hash of the input string
    md5_hash = calculate_md5(input_string)

    # Print the original string and its MD5 hash
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")
