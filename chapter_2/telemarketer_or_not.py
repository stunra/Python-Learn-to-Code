# https://dmoj.ca/problem/ccc18j1

_1 = int(input())
_2 = int(input())
_3 = int(input())
_4 = int(input())

if (_1 == 8 or _1 == 9) and (_4 == 8 or _4 == 9) and (_2 == _3):
	print('ignore')
else:
	print('answer')
