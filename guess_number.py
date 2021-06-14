import random
guess_number = random.randint(1, 100)
print("guess number (1~100)")
num = int(input())
while num != guess_number:
    if num < guess_number:
        print("go up")
    else:
        print("go down")
    num = int(input())
else: print(f"That's right! The number was {guess_number}.")
