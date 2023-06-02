N, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

arr.sort()  # Sort the array in ascending order

cumulative_sum = [0]
for i in range(N):
    cumulative_sum.append(cumulative_sum[i] + arr[i])

cost = []

def binary_search_lower_bound(q):
    low = 0
    high = N
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < q:
            low = mid + 1
        else:
            high = mid
    return low

for q in queries:
    idx = binary_search_lower_bound(q)
    left_cost = q * idx - cumulative_sum[idx]
    right_cost = cumulative_sum[N] - cumulative_sum[idx] - q * (N - idx)
    total_cost = left_cost + right_cost
    cost.append(total_cost)

print(*cost)
