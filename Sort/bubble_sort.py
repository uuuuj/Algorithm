import sys
from typing import MutableSequence

# 함수의 매개변수로, a라는 가변 시퀀스를 받습니다. MutableSequence는 가변 시퀀스 자료형을 나타내는 것으로, 이 매개변수는 리스트나 배열 등을 의미합니다.
# -> None: 함수의 반환값이 없음을 나타냅니다.
def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    # 패스
    for i in range(n-1):
        # j를 n-1부터 i+1까지 1씩 감소시킨다
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(sys.stdin.readline())
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x) #배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')