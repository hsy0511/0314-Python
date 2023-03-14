# 불
a = True # 불 자료형은 Ture와 False 값만 가진다.(True나 False는 파이썬의 예약어로 첫 문자를 항상 대문자로 사용해야 한다.)
b = False
print(type(a))
print(type(b)) # type함수를 통해서 불 자료형으로 되어있는지 파악한다.
1 == 1 # Ture
2 > 1 # Ture
1 < 2 # False
# 예시
if [] :
    print("참")
else :
    print("거짓")
    
if [1,2,3] :
    print("참")
else :
    print("거짓")


print(bool("candy"))
print(bool(""))
print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(3))
print(bool((1,2,3)))
print(bool(()))
print(bool({1,2,3}))
print(bool(None))
