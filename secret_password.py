```py
my_google_pass = "IamMorrisJKL001342"
key_scene1 = 13
safe_storage = caesar_cipher(my_google_pass, key_scene1, 'encrypt')
print(f"儲存於文字檔的加密密碼: {safe_storage}")
print(f"當我要登入 Google 時還原: {caesar_cipher(safe_storage, key_scene1, 'decrypt')}\n")
```
