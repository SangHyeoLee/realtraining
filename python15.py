word = ('banana')
end = 0
for i in word:
    if i == 'a':
        break
    end += 1
    if end == range(len(word)):
        end = -1
print(end)