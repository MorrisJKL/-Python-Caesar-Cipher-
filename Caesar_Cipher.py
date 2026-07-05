```py
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha(): 
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result
secret_key = 7
test_text = "Hello, I'm MorrisJKL!"
encrypted = caesar_cipher(test_text, secret_key, 'encrypt')
decrypted = caesar_cipher(encrypted, secret_key, 'decrypt')
print(f"原始文字: {test_text}")
print(f"加密結果: {encrypted}")
print(f"解密結果: {decrypted}")
```
