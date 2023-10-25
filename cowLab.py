def encode(password_encode):
    encoded = []
    for i in password_encode:
        l = int(i)
        if l < 7:
            l = l + 3
        elif l == 7:
            l = 1
        elif l == 8:
            l = 2
        elif l == 9:
            l = 3
        l = str(l)
        encoded.append(l)
    encoded2 = ''.join(map(str, encoded))
    return encoded2

def decode(password):
    return ''.join(str((int(i) - 3) % 10) for i in password)

def main():
    encoded = None
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        answer = int(input("Please enter an option: "))
        if answer == 1:
            encoded = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif answer == 2:
            if encoded is None:
                print("No password has been encoded!\n")
            else:
                decoded = decode(encoded)
                print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")
        elif answer == 3:
            break

if __name__ == "__main__":
    main()
