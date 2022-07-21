T = int(input())
for i in range(1, T+1):
    
    s = str(i)
    output=""
    check = 0
    for j in range(0,len(s)):
        if s[j] in ['3','6','9'] :
            check = 1
            output+="-"
            
    if check == 1:
        print(output,end=" ")
    else:
        print(i,end = " ")