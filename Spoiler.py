movie_spoiler = "Do you know Morris marry the guy who steal Ellan's bag at the end of the movie!"
key_scene2 = 5

post_on_forum = caesar_cipher(movie_spoiler, key_scene2, 'encrypt')
print(f"發布在討論區的貼文: {post_on_forum}")
print(f"讀者點擊「顯示暴雷內容」後解密: {caesar_cipher(post_on_forum, key_scene2, 'decrypt')}\n")
