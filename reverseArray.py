def reverseArray(a):
    reverse=[]
    for i in range(len(a)-1,-1,-1):
        reverse.append(a[i])
    return reverse

x=reverseArray([1,2,3,4])
print(x)