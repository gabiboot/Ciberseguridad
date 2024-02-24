import hashlib

def calculate_checksum(file_path, algorithm="sha256"):
    hash_function = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_function.update(byte_block)
    return hash_function.hexdigest()

file_path = "C:\Users\gmoya\Downloads\pycharm-professional-2023.3.3.exe"
checksum = calculate_checksum(file_path)
print("SHA-256 checksum:", checksum)