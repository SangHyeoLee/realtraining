# 저수 number가 주어질 때, 각 자릿수의 합을 구해서 출력해보세요
number = 123
result = 0
while number:
  #몫은 다음 number가 됨.
  #나머지는 더해나가면 된다!.
  result += number%10
  number //=10
print(result)

