number = 1234
mod = 1000
list = []

while mod > 0:
    list.append(number// mod)
    number %= mod
    mod = mod // 10
print(*list[::-1], sep='')