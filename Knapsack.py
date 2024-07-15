def subset_sum(n, k, arr):
    possiblesums = [0] * (k + 1)
    for i in range(1, k + 1):
        for num in arr:
            if num <= i:
                possiblesums[i] = max(possiblesums[i], possiblesums[i - num] + num)
    return possiblesums[k]

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(subset_sum(n, k, arr))
