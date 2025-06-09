
# Import the SHA3_256 hash algorithm from the Crypto.Hash module
from Crypto.Hash import SHA3_256

def sha3(message):
    """
    Calculates the SHA3-256 hash of the given message.

    Args:
        message (bytes): The input data (as bytes) to be hashed.

    Returns:
        bytes: The SHA3-256 hash as a bytes object.
    """
    # Create a new SHA3-256 hash object
    sha3_hash = SHA3_256.new()
    
    # Update the hash object with the message.
    # The message should already be in bytes format.
    sha3_hash.update(message)
    
    # Return the digest (hash value) as a bytes object
    return sha3_hash.digest()

def main():
    """
    Main function to get user input, calculate SHA3 hash, and print the results.
    """
    # Get text input from the user and encode it to bytes using UTF-8
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    
    # Calculate the SHA3 hash of the encoded text
    hashed_text = sha3(text)
    
    # Print the original input text (decoded back to string for display)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    
    # Print the SHA3 hash in hexadecimal format
    print("SHA-3 Hash:", hashed_text.hex())

# This block ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()
