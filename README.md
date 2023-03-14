# 0314-Python
# 딕셔너리 자료형 
### 딕셔너리는 중복을 허용하지 않고 순서가 없다는 특징을 가지고 있다.(인덱싱을 할 수 없음)
### 딕셔너리는 {}를 사용하고 각각 key:value 형태로 이루어져있다.
```python
a = {1:'hello',2:'world'} # 딕셔너리{} 안에 각각의 요소가 key:value 형태로 이루어져있다.
print(a)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224892851-090318b0-7e77-4435-90eb-436feaf8ea5f.png)

### 딕셔너리의 value 값에 리스트 넣기 . (key 안에는 리스트 삽입이 불가능 함.)
```python
a = {1:'hello',2:'world',3:[1,2,3]} # 딕셔너리{} value 안에 리스트도 넣을 수 있다.(key 안에 리스트는 못 들어감)
print(a)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224892896-ec0ab6d3-aaf8-4215-99b7-8013c8bb68fd.png)
### 딕셔너리 안에 쌍 추가하기.(x[y]안에 y는 문자와 리스트로도 사용이 가능하다.)
```python
b = {1:'good'}
b[2] = 'a' # b 딕셔너리{} 안에 각각 key = 2, value = a 라는 딕셔너리 쌍을 추가했다. (b[x]안에 x는 문자와 리스트로도 사용이 가능하다.)
print(b)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224892950-bacd3dde-f8bd-4da7-85cc-a3289edd6e24.png)
### del 함수를 사용하여 딕셔너리에 n번째 값 지우기(모든 쌍을 지우기 위해서는 .clear 함수를 사용한다.)
```python
c = {1:'a',2:'b',3:'c',4:'d'}
del c[2]
print(c) # c 딕셔너리{}에 2번째 쌍를 삭제했다.(모든 쌍을 지우려면 .clear라는 함수를 사용하면 된다.)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224893577-f71e6b46-18e0-4820-b51a-d6c7f204866f.png)
### key를 통해 value 값 찾기
```python
d = {1:'a',2:'b',3:'c'}
print(d[2])
"""
d 딕셔너리{}에 2번째 딕셔너리 value 값을 key를 통해 찾아냈다.(.get(key) 함수를 써도 value 값을 찾을 수 있다. )
 .get(key) 함수를 사용할 때 딕셔너리 안에 존재하지 않은 key를 입력하면 none 을 리턴하고 .get[key] 라고 쓰면 오류가 발생한다.
 딕셔너리 안에 key가 없을 경우 미리 정해둔 디폴트 값을 가져오기 위해서 .get(x,디폴트 값)을 사용하면 된다.
"""
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224893622-efae2cc7-5e71-49ec-b810-ffe2ee336b93.png)
### 딕셔너리 안에 중복되는 key가 있으면 하나를 제외한 모든 중복 key는 사라진다.
```python
e = {1:'a',1:'b'} # 한 딕셔너리{} 안에 같은 값에 key가 들어가있으면 하나를 제외한 모든 key는 사라진다.
print(e)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224893660-c871427a-2f08-4fc1-a676-29ccc1ea81ac.png)
### keys 함수를 사용하여 딕셔너리 안에 key들을 리스트로 바꾸기(value는 values 함수를 쓴다.)
```python
f = {1:'a',2:'b',3:'c'} 
print(f.keys()) # .keys함수는 딕셔너리{} 안에서 key를 모아서 리스트로 만들었다.(.values를 하면 value를 모아 리스트를 만들어준다.)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224893752-a86ed872-8dff-43f3-8c28-46f2714f8c57.png)

### items 함수를 사용하여 딕셔너리 안에있는 쌍 얻기
```python
g = {1:'hello',2:'world'}
print(g.items()) # .items함수는 딕셔너리{} 안에있는 쌍을 얻는다.
```
### 결과 값

![image](https://user-images.githubusercontent.com/104752580/224893784-800ba0c3-6d0c-4abd-b0c5-f68d11b520d9.png)
### in 함수를 이용해 해당 key가 딕셔너리 안에 있는지 조사하기(존재하면 ture 존재하지 않으면 false를 나타냄)
```python
h = {1:'a',2:'b',3:'c'} 
print(1 in h) # in은 해당 key가 딕셔너리{} 안에 존재하는지 조사한다.(존재하면 ture, 존재하지 않으면 false를 리턴한다.)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224893886-8ceea69a-11a7-4630-bbe1-eb9e71a132b3.png)
# 집합 자료형
### 집합은 중복을 허용하지 않고 순서가 없다는 특징을 가지고 있다.(인덱싱을 할 수 없음)
### 집합은 set()으로 나타낸다.(숫자를 나타낼때는 [],{} 둘중에 하나로 반드시 감싸야한다.)
```python
a = set([1,2,3]) # 집합은 set으로 나타낸다.(숫자는 [],{} 둘중에 하나로 반드시 감싸야한다.)
print(a)
b = set('apple') # 집합은 중복을 허용하지 않고 순서가 없다는 특징을 가지고 있다.
print(b)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224894468-daa46f40-f5ad-4697-bfcb-a134d91e2f10.png)
### 집합 연산하기
```python
c1 = set([2,4,6,8,10,12,14,16,18])
c2 = set([3,6,9,12,15,18])
c = c1 & c2 # &는 교집합을 나타냄
d = c1 | c2 # |는 합집합을 나타냄
e = c1 - c2 # -는 차집합을 나타냄
print(c)
print(d)
print(e)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224894521-86368219-332f-4971-b556-83abd4d1c901.png)
### add 함수로 집합에 1개의 값 추가하기(여러개을 추가하고 싶은때는 update를 사용한다.)
```python
f = set([1,2,3])
f.add(4) # add함수는 집합에 1개의 값을 추가한다.(.update는 여러개의 값을 추가하는 함수이다.)
print(f)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224894576-3976bddc-74bd-42a9-ba81-f31e7de25b12.png)
### remove 함수로 특정 값 제거하기 
```python
g = set([1,2,3])
g.remove(1) # remove 함수는 특정 값을 제거한다.
print(g)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224894604-d1267537-d29b-46dd-9f01-1f52df026135.png)
# 불 자료형
### 불 자료형은 Ture와 False 값만 가진다.(True나 False는 파이썬의 예약어로 첫 문자를 항상 대문자로 사용해야 한다.)
```python
a = True # 불 자료형은 Ture와 False 값만 가진다.(True나 False는 파이썬의 예약어로 첫 문자를 항상 대문자로 사용해야 한다.)
b = False
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224894774-ccee4fc0-e954-4d51-9e37-3182fe0661a8.png)
### type 함수를 사용하여 불 자료형인지 파악하기
```python
print(type(a))
print(type(b)) # type함수를 통해서 불 자료형으로 되어있는지 파악한다.
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224894806-cf0832d7-68c3-424d-b172-f06cb69fe7af.png)
### 불 자료형의 참과 거짓
![image](https://user-images.githubusercontent.com/104752580/224891277-b4d5dc14-9181-4c20-bc97-1f2d96b188b1.png)
### 예시
```python
if [] :
    print("참")
else :
    print("거짓")
    
if [1,2,3] :
    print("참")
else :
    print("거짓")
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224894953-860dacf1-1191-4eab-9613-380b4a7d2b0b.png)

```python
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
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224894976-848ed012-0041-4e86-af65-c6351edd06dc.png)
# 자료형의 값을 저장하는 공간, 변수
### 파이썬은 java,c언어와 다르게 자료형 타입을 선언하지않는다.(변수의 저장된 값을 스스로 판단하여 자료형 타입을 지정함.)
```python
a = 1
b = "hello world"
c = [1,2,3] # 파이썬은 java,c언어와 다르게 자료형 타입을 선언하지않는다.(변수의 저장된 값을 스스로 판단하여 자료형 타입을 지정함.)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224895348-7930ba46-685e-4b4f-9a05-835b1362110e.png)
### id 함수로 메모리 주소 값 가르키기
```python
a = [1,2,3]
print(id(a)) # a가 가르키는 메모리 주소를 가르킨다.
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224895425-08c083ab-9d94-4ebf-a8ea-ed9dead6e0dd.png)
### 리스트 복사하고 id,is 함수로 동일한 값인지 확인하기
```python
a = [1,2,3]
b = a # 리스트 자료형을 복사하는 예시이다.
print(id(a))
print(id(b)) # 메모리주소로 완전히 동일한지 파악한다.
print(a is b) # is를 써서 동일한지 파악한다.
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224895481-c2b76ae6-fa28-4b32-8a60-27f911ea2f93.png)
### 기존 리스트 값을 바꿔도 복사한 데이터의 변함이 없는지 확인하기
```python
a = [1, 2, 3]
b = a[:]
a[1] = 4 # a리스트를 바꿔도 b 리스트에는 변함이 없는지 파악한다.
print(a)
print(b)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224895500-91c11965-a3a2-4510-926b-f612ee66f109.png)
### copy 함수로 리스트 복사 후 is 함수로 동일한 값인지 확인하기
```python
from copy import copy # copy 함수를 사용하기 위해 iport 시킨다.
a = [1,2,3]
b = copy(a) # b에서 copy 함수를 통해서 a를 복사한다.
print (b is a) # is를 써서 동일한지 파악한다.
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224895614-5a9819db-1ecf-43de-bd4a-341f7c4aa59f.png)
### 변수를 여러가지 방법으로 만들기
```python
a,b = ('c','d') # 튜플로 a,b 값을 대입한다.
(a,b) = 'c','d'  # 튜플은 ()가 필요 없다.
[a,b] = ['c','d'] # 리스트로도 변수를 만들 수 있다.
a = b = 'c' # 여러개의 변수에 같은 값을 넣을 수 있다.
a = 3
b = 5
a,b = b,a
print(a)
print(b) # 두 변수의 값을 간단하게 바꿀 수 있다.
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224895670-1c951fd1-7581-4689-ab99-b88ea5a244ca.png)
# quiz
### 조건에 맞게 작성
![image](https://user-images.githubusercontent.com/104752580/224913119-8e4fd646-a87c-49e1-8767-9f9211998e9b.png)
### 나의 코드 
```python
from random import * # random 모듈 import
a = range(1,21) # 1~20까지 범위 설정
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # 1~20까지 리스트 작성
print(type(a)) # a 자료형 형태 파악
print(type(b)) # b 자료형 형태 파악
print(list(a)) # a 자료형 리스트로 변환
shuffle(b) # b 리스트 값 혼합하여 섞기
print(b)
print('---당첨자 발표---')
c = sample(b,1) # b 자료형에서 1개 랜덤으로 뽑고 리스트로 변환
print('치킨 당첨자 : ',end='') # ,end=''를 통해 한줄로 붙여쓰기 (\n과 같음) 
print(c[0]) # c의 0번째 인덱스 값 인덱싱
print('커피 당첨자 : ',end='')
print(sample(a,3)) # a 자료형에서 3개 랜덤으로 뽑고 리스트로 변환
print('----축하합니다----')
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/224912850-67df02f7-769d-43da-ad56-e13e776aab22.png)


