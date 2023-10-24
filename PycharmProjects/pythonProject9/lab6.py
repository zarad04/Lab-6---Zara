# Zara Dalvi

def encode(password):
    encoded_pass = ""
    for i in password:
        increased_digit = str(int(i) + 3)
        encoded_pass += increased_digit
    return encoded_pass



stored_pass = ""

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    menu_option = int(input("Please enter an option: "))


    if menu_option == 1:
        password = input("Please enter your password to encode: ")
        encoded = encode(password)
        stored_pass += encoded
        print("Your password has been encoded and stored!\n")

    elif menu_option == 2:
        pass


    elif menu_option == 3:
        break

