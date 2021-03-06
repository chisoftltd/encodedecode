alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_amount):
	cipher_text = ''
	for letter in plain_text:
		position = alphabet.index(letter)
		new_position = position + shift_amount
		cipher_text += alphabet[new_position]

	print(f"The encoded text is \'{cipher_text}\'")

def decrypt(text, shift):
	cipher_text = ''
	for letter in text:
		position = alphabet.index(letter)
		new_position = position - shift
		cipher_text += alphabet[new_position]
	print(f"The decoded text is \'{cipher_text}\'")

if direction == 'encode':
	encrypt(text, shift)
elif direction == 'decode':
	decrypt(text, shift)
else:
	print("Wrong option selected. Type 'encode' or 'decode'")