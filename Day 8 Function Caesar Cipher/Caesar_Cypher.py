alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


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


def decrypt(text_input, shift_in):
    solved_text = ""
    for x in text_input:
        position = alphabet.index(x)
        new_position = position - shift_in
        solved_text += alphabet[new_position]
    print(f"The Solved Solution is {solved_text}!\n")


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.[Ans: list Index out of range, possible to fix with an numpy array instead]
choice = True
while choice:
    # encrypt(text, shift)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print(f"{direction} Error Not a Valid Command!")

    Rerun = input("Continue? Type Y/N\n")
    if Rerun == "Y" or Rerun == "y":
        continue
    else:
        break
