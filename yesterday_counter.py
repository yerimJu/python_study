f = open("yesterday.txt","r")
yesterday_lyric = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()
print(yesterday_lyric)
print(f"Number of a word 'yesterday': {yesterday_lyric.lower().count('yesterday')}")
