t = int(input())
for i in range(t):
    f = input()
    if f == f[::-1]:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")