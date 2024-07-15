n = int(input())
for _ in range(n):
    input_str = input()
    visited = set()
    cost = 0    
    for char in input_str:
        if char not in visited:
            cost += 1
            visited.add(char)
    print(cost)
