print("구구단 몇 단을 계산할까요?")
num = int(input())
print(f"구구단 {num}단을 계산합니다.")
for i in range(1, 10):
    print(f"{num}*{i}={num*i}")
