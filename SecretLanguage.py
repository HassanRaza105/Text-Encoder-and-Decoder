try:
    import pyperclip
except ImportError:
    pyperclip = None


def encode_str(inputString):
    import random
    import string

    inputStringList = inputString.split()
    encoded_string_list = []
    for word in inputStringList:
        if len(word) > 3:
            word = word + word[0:1]
            word = word[1:]
        word = (
            "".join(random.sample(string.ascii_letters, 3))
            + word
            + "".join(random.sample(string.ascii_letters, 3))
        )
        encoded_string_list.append(word)
    final_string = " ".join(encoded_string_list)
    # pyperclip.copy(final_string)
    if pyperclip:
        pyperclip.copy(final_string)

    return final_string


def decode_str(inputString):

    inputStringList = inputString.split()
    decoded_string_list = []
    for word in inputStringList:
        word = word[3:-3]
        if len(word) > 3:
            word = word[-1] + word
            word = word[0:-1]
        decoded_string_list.append(word)
    final_string = " ".join(decoded_string_list)
    # pyperclip.copy(final_string)
    if pyperclip:
        pyperclip.copy(final_string)

    return final_string


choice = int(input("Please Enter 1 for Encoding and 2 for Decoding: "))
user_input = input("Please Enter a sentence: ")

if choice == 1:
    print(encode_str(user_input))
elif choice == 2:
    print(decode_str(user_input))
else:
    print("Wrong Choice")
