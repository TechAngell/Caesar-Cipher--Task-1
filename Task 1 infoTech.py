def caesar_cipher(text, shift, mode):
 
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  new_text = '' 
  for char in text:
    if char.isalpha():
      index = alphabet.find(char)
      new_index = (index + shift) % len(alphabet)
      new_char = alphabet[new_index]
    else:
      new_char = char
    new_text += new_char
  return new_text

def main():
  
  while True:
    print("Enter 'e' to encrypt or 'd' to decrypt:")
    mode = input().lower()
    if mode in ('e', 'd'):
      break
    else:
      print("Invalid mode. Please enter 'e' or 'd'.")

  message = input("Enter your message: ")
  shift = int(input("Enter the shift value: "))

  if mode == 'e':
    encrypted_text = caesar_cipher(message, shift, mode)
    print("Encrypted message:", encrypted_text)
  else:
    decrypted_text = caesar_cipher(message, -shift, mode)
    print("Decrypted message:", decrypted_text)

if __name__ == "__main__":
  main()
