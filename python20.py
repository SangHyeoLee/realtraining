n= 123
x=str(n)
sum1=0
sum2=0
for i in x:
  sum1+=int(i)
print(sum1)

def solution(n):
    answer=0
    while n>0 :
        answer+=n%10
        n//=10
    return answer

print(solution(n))
