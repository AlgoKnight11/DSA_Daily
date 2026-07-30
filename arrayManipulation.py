def arrayManipulation(n, queries):
    # Write your code here
    results=[0]*(n+2)
    for a,b,k in queries:
        results[a]+=k
        results[b+1]-=k
    max_value=0
    current_sum=0
    for i in range(0,n+1):
        current_sum+=results[i]
        if current_sum>max_value:
            max_value=current_sum
    return max_value
print(arrayManipulation(10,[[1,5,3],[4,8,7],[6,9,1]]))