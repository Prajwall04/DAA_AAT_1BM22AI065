def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + mid + quicksort(right)

n = int(input())
arr = list(map(int, input().split()))
ans = quicksort(arr)

for num in ans:
    print(num, end=' ')
