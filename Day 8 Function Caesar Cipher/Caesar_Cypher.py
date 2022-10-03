alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_input, shift_in):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift
    #  amount and print the encrypted text.
    new_text = ""
    for letter in text_input:
        # index method to move alphabets
        position = alphabet.index(letter)
        new_position = position + shift_in
        new_letter = alphabet[new_position]

        new_text += new_letter
    print(f"The encoded text is {new_text}")


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.[Ans: list Index out of range, possible to fix with an numpy array instead]
choice = True
while choice:
    encrypt(text, shift)
    Rerun = input("Continue? Type Y/N\n")
    if Rerun == "Y":
        print(f"Continue with {choice}")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

    else:
        choice = False
