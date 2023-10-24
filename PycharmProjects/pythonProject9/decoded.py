
def decode(encoded_pass):
    decoded_pass = ""
    for i in encoded_pass:
        decreased_digit = str(int(i) - 3)
        decoded_pass += decreased_digit
    return decoded_pass

if menu_option == 2
decoded = decode(stored_pass)
        print(f'The encoded password is {stored_pass}, and the original password is {decoded}.')