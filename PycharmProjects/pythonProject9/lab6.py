# Zara Dalvi

def encode(password):
    encoded_pass = ""
    for i in password:
        increased_digit = str(int(i) + 3)
        
        # adding handling for encoded values with 2 digits to roll over - Brandon
        if int(increased_digit) > 9:
            increased_digit = str(int(increased_digit) - 10)
             
        encoded_pass += increased_digit
    return encoded_pass



# adding decode function - Brandon
def decode(encoded):
    return ''.join(list(map(lambda x: str((int(x) - 3) % 10), encoded)))



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
        
        # changed from += to = because it does not appear we would want to add 
        # multiple passwords together if we pass through the loop multiple times
        stored_pass = encoded
        print("Your password has been encoded and stored!\n")
        
    # added logic for handling decode - Brandon
    elif menu_option == 2:
        decoded = decode(stored_pass)
        output = "The encoded password is {}, and the original password is {}.".format(stored_pass, decoded)
        print(output)

    elif menu_option == 3:
        break

