import hashlib
string = "fkylfhsq".encode()
print("Original hash: ", hashlib.md5(string).hexdigest())
#first iteration to enter while loop
i = 0
hasher = hashlib.md5(string + str(i).encode())

for k in range(8):
    while not(hasher.hexdigest().startswith("00000")):
        i += 1
        hasher = hashlib.md5(string + str(i).encode())
    print(f"Calculated hash: {hasher.hexdigest()}\nResult number: {i}")
    i += 1
    hasher = hashlib.md5(string + str(i).encode())