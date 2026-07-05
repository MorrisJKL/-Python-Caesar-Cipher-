# 基於 Python 之多元生活場景凱薩密碼（Caesar Cipher）應用實作

Colab: https://colab.research.google.com/drive/1dU0a1L3OruK6w_DC34jtihzZBhlR_eRG?usp=sharing

## 1. 核心程式碼實作
這個程式支援英文大小寫加密與解密，並會自動忽略數字、空格與中文字（保持原樣），非常適合用來處理日常文字。

<img width="685" height="447" alt="image" src="https://github.com/user-attachments/assets/fdd2de2a-6c0d-4c5b-b2ab-abfa9c97529c" />


## 2. 實例運用場景
我設計了三個不同的應用情境，並直接用 Python 模擬出來：

### 場景一：防君子不防小人的「密碼筆記本」
情境說明：
很多人會把 Google、Discord 或遊戲帳號的密碼記在電腦的 password.txt 裡面，但這很容易被借用電腦的朋友一覽無遺。我們可以透過凱薩密碼，將密碼轉換成一堆亂碼。雖然擋不住專業駭客，但可以有效防止身邊朋友的「不小心偷瞄」。

<img width="702" height="162" alt="image" src="https://github.com/user-attachments/assets/1a2d4b9f-fd6f-4b61-add0-6e37cb200499" />



### 場景二：社群軟體上的「防暴雷（Spoiler）機制」
情境說明：
在社群平台（如 Discord 或 Thread 討論區）分享最新電影的劇情時，為了不讓還沒看過的人被暴雷，可以用金鑰 5 加密。想看的人只要複製密碼、貼進解密工具就能觀看。

<img width="857" height="171" alt="image" src="https://github.com/user-attachments/assets/3ef6ca16-4c2f-4809-a158-56d1e8fa1452" />




### 場景三：獨立遊戲開發的「關卡彩蛋與解答隱藏」
情境說明：
我用 Python 寫了一款解謎遊戲，遊戲的「通關密碼」或說「隱藏彩蛋」直接寫在程式碼裡，只要打開原始碼（原始碼流出）就會直接看到答案。我使用凱薩密碼，可以將答案混淆，讓玩家自行看 code 破解的難度。

<img width="573" height="200" alt="image" src="https://github.com/user-attachments/assets/df4b7cf2-f876-4721-aad1-9ce3ff70fe06" />



## 3. 心得

這個小型專案讓我體會到資安的兩大核心原則：
- 機密性（Confidentiality）： 透過演算法將明文轉換為密文，確保未授權者無法直接讀取。
- 金鑰管理（Key Management）： 在凱薩密碼中，位移量（Shift）就是金鑰。如果金鑰外洩，再複雜的密文也會被輕易破解。

## 學習資料:

1. 凱薩密碼/加密/解密【一起學習 麥塊破解方法。 方程島兒童程式學苑（2025)。
https://www.youtube.com/watch?v=jzaL8pEFmGU
2. 一起學加密(3)——Python實現凱薩加密。 麦兜搞IT (2022)。
https://www.youtube.com/watch?v=EUhI0-v2Ps0

