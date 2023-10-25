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


if __name__ == "__main__":
    running = True
    while running:
        print(f"Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        answer = int(input("Please enter an option: "))
        if answer == 1:
            password_encode = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        elif answer == 2:
            coded = encode(password_encode)
            print(f"The encoded password is {coded}, and the original password is {password_encode}.\n")
        elif answer == 3:
            running = False



