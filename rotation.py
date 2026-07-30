def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        x=arr.pop(0)
        arr.insert(len(arr),x)
    return arr
print(rotateLeft(2,[1,2,3,4,5,6]))