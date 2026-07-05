encrypted_answer = "Xoqbu" 
key_scene3 = 22
player_input = input("請輸入通關密碼（請輸入 Bingo 試試看）：")
if caesar_cipher(player_input, key_scene3, 'encrypt') == encrypted_answer:
    print("恭喜通關！解鎖隱藏彩蛋！")
else:
    print("密碼錯誤，再試一次！")
