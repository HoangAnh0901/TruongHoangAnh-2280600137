
import hashlib

def blake2(message):
    """
    Calculates the BLAKE2b hash of the given message.
    This function takes a message (as bytes) and returns its BLAKE2b hash.
    BLAKE2b is a cryptographic hash function, designed to be faster than SHA-3
    and comparable to SHA-2, while offering strong security properties.
    The 'digest_size=64' parameter specifies that it will produce a 512-bit (64-byte) hash.

    Args:
        message (bytes): The input data (as bytes) to be hashed.

    Returns:
        bytes: The BLAKE2b hash as a bytes object.
    """
    # Create a new BLAKE2b hash object with a digest size of 64 bytes (512 bits)
    blake2_hash = hashlib.blake2b(digest_size=64)
    
    # Update the hash object with the message.
    # The message should already be in bytes format.
    blake2_hash.update(message)
    
    # Return the digest (hash value) as a bytes object
    return blake2_hash.digest()

def main():
    """
    Main function to get user input, calculate BLAKE2b hash, and print the results.
    """
    # Get text input from the user and encode it to bytes using UTF-8
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    
    # Calculate the BLAKE2b hash of the encoded text
    hashed_text = blake2(text)
    
    # Print the original input text (decoded back to string for display)
    print("Chuỗi văn bản đã nhập:", text.decode("utf-8"))
    
    # Print the BLAKE2b hash in hexadecimal format
    print("BLAKE2 Hash:", hashed_text.hex())

# This block ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()
