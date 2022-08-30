alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher):
    ciphered_text = ""
    shift_amount = shift_amount % len(alphabet)
    if cipher == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet:
            ciphered_text += letter
        else:
            letter_index = alphabet.index(letter)  # gives the integer value of each letter's index
            ciphered_index = letter_index + shift_amount
            if ciphered_index > 25:
                ciphered_index = ciphered_index % len(alphabet)
            ciphered_letter = alphabet[ciphered_index]
            ciphered_text += ciphered_letter
    print(f"Your {cipher}d text is \"{ciphered_text}\".")


user = True
while user:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher=direction)
    x = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if x == "yes":
        user = True
    else:
        user = False
        print("Goodbye.")
