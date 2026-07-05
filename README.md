# 基於 Python 之多元生活場景凱薩密碼（Caesar Cipher）應用實作

## 1. 核心程式碼實作
這個程式支援英文大小寫加密與解密，並會自動忽略數字、空格與中文字（保持原樣），非常適合用來處理日常文字。

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

## 2. 實例運用場景
我設計了三個不同的應用情境，並直接用 Python 模擬出來：

### 場景一：防君子不防小人的「密碼筆記本」
情境說明：
很多人會把 Google、Discord 或遊戲帳號的密碼記在電腦的 password.txt 裡面，但這很容易被借用電腦的朋友一覽無遺。我們可以透過凱薩密碼，將密碼轉換成一堆亂碼。雖然擋不住專業駭客，但可以有效防止身邊朋友的「不小心偷瞄」。

```py
my_google_pass = "IamMorrisJKL001342"
key_scene1 = 13
safe_storage = caesar_cipher(my_google_pass, key_scene1, 'encrypt')
print(f"儲存於文字檔的加密密碼: {safe_storage}")
print(f"當我要登入 Google 時還原: {caesar_cipher(safe_storage, key_scene1, 'decrypt')}\n")
```


### 場景二：社群軟體上的「防暴雷（Spoiler）機制」
情境說明：
在社群平台（如 Discord 或 Thread 討論區）分享最新電影的劇情時，為了不讓還沒看過的人被暴雷，可以用金鑰 5 加密。想看的人只要複製密碼、貼進解密工具就能觀看。

```py
movie_spoiler = "Do you know Morris marry the guy who steal Ellan's bag at the end of the movie!"
key_scene2 = 5

post_on_forum = caesar_cipher(movie_spoiler, key_scene2, 'encrypt')
print(f"發布在討論區的貼文: {post_on_forum}")
print(f"讀者點擊「顯示暴雷內容」後解密: {caesar_cipher(post_on_forum, key_scene2, 'decrypt')}\n")
```

### 場景三：獨立遊戲開發的「關卡彩蛋與解答隱藏」
情境說明：
我用 Python 寫了一款解謎遊戲，遊戲的「通關密碼」或說「隱藏彩蛋」直接寫在程式碼裡，只要打開原始碼（原始碼流出）就會直接看到答案。我使用凱薩密碼，可以將答案混淆，讓玩家自行看 code 破解的難度。
```py
encrypted_answer = "Xoqbu" 
key_scene3 = 22
player_input = input("【遊戲關卡】請輸入通關密碼（請輸入 Bingo 試試看）：")
if caesar_cipher(player_input, key_scene3, 'encrypt') == encrypted_answer:
    print("恭喜通關！解鎖隱藏彩蛋！")
else:
    print("密碼錯誤，再試一次！")
```

## 3. 心得

這個小型專案讓我體會到資安的兩大核心原則：
- 機密性（Confidentiality）： 透過演算法將明文轉換為密文，確保未授權者無法直接讀取。
- 金鑰管理（Key Management）： 在凱薩密碼中，位移量（Shift）就是金鑰。如果金鑰外洩，再複雜的密文也會被輕易破解。

## 學習資料:

1. 凱薩密碼/加密/解密【一起學習 麥塊破解方法。 方程島兒童程式學苑（2025)。
https://www.youtube.com/watch?v=jzaL8pEFmGU
2. 一起學加密(3)——Python實現凱薩加密。 麦兜搞IT (2022)。
https://www.youtube.com/watch?v=EUhI0-v2Ps0

