def arrayManipulation(n, queries):
    # Write your code here
    results=[0]*n
    for i in queries:
        for j in range(i[0]-1,i[1]):
            results[j]=results[j]+i[2]
    return max(results)
print(arrayManipulation(10,[[1,5,3],[4,8,7],[6,9,1]]))