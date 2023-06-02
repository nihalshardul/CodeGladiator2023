n, m = [int(x) for x in input().split()] 
arr = list(map(int,input().split())) 
queries = list(map(int,input().split())) 
cost = []

#for i in range(len(queries)):
#    c=0
#    for j in range(len(arr)):
#        c+=abs(queries[i]-arr[j])
#    cost.append(c)

for query in queries:
    c = sum(abs(query - num) for num in arr)
    cost.append(c)

print (*cost)
