from typing import MutableSequence
import sys

N = int(sys.stdin.readline())

a = [0] * N
sorted_a = [0] * N
def merge_sort(a: MutableSequence, m, mid, n) -> None:
    i = m
    j = mid + 1
    k = m
    #작은 순서대로 배열에 삽입
    while i <= mid and j <= n:
        if a[i] <= a[j]:
            sorted_a[k] = a[i]
            i += 1
        else:
            sorted_a[k] = a[j]
            j += 1
        k += 1
    if i > mid:
        t = j
        for t in range(t, n+1, 1):
            sorted_a[k] = a[t]
            k += 1
    else:
        t = i
        for t in range(t, mid+1, 1):
            sorted_a[k] = a[t]
            k += 1
    t = m
    for t in range(t, n+1, 1):
        a[t] = sorted_a[t]

#2분할 정렬한걸 모아준다.
def merge_sort2(a: MutableSequence, m, n) -> None:
    #배열의 크기가 1인 경우를 제외하고
    if m < n:
        mid = (m + n) // 2
        #m부터 mid까지 나눈다
        merge_sort2(a, m, mid)
        #mid부터 n까지 나눈다
        merge_sort2(a, mid+1, n)
        #합쳐준다
        merge_sort(a, m, mid, n)

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

merge_sort2(arr, 0, N-1)

for i in a:
    print(i)