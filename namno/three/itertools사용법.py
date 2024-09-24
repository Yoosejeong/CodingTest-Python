#코테문제 아닌 itertools 사용방법
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product

#combinations(iterable, r) : iterabe에서 원소 개수가 r개인 조합 뽑기

list = [1,2,3]

for i in combinations(list, 2):
    print(i)
    #(1,2) (1,3) (2,3)

#combinations_with_replacement(iterable, r) : iterable에서 원소 개수가 r개인 중복 조합 뽑기

list = ['A', 'B', 'C']

for i in combinations_with_replacement(list, 2):
    print(i)
    #('A', 'A') ('A', 'B') ('A', 'C') ('B', 'B') ('B', 'C') ('C', 'C')

#permutations(iterable, r=None) : iterable에서 원소 개수가 r개인 순열 뽑기

for i in permutations(list, r=None) : #r을 지정하지 않거나, r=None이면 최대 길이의 순열이 리턴
    print(i)
    #('A', 'B', 'C') ('A', 'C', 'B') ('B', 'A', 'C') ('B', 'C', 'A') ('C', 'A', 'B') ('C', 'B', 'A')

#produec(*iterables, repeat=1) : 여러 iterable의 데카르트곱 리턴
#다른 함수와 달리 인자로 여러 iterable넣을 수 있고, 그 친구들간 모든 짝 지어서 리턴

list1 = ['A', 'B']
list2 = ['1', '2']

for i in product(list1, list2, repeat=1) : #list1과 list2의 모든 쌍을 지어 리턴
    print(i)
    #('A', '1') ('A', '2') ('B', '1') ('B', '2')

