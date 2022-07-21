t = int(input())

for i in range(t):
    h1, m1, h2, m2, = map(int,input().split())
    
    H = h1 + h2
    M = m1 + m2
    if M >= 60:
        M -= 60
        H += 1
    if H > 12:
        H -= 12
    else:
        H
print(f"#{i+1} {H} {M}")
