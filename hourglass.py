def hourglassSum(arr):
    # Write your code here
    hourglass=[]
    glass_sum=[]
    for i in range(0,4):
        for j in range(0,4):
            values=[]
            for k in range(0,3):
                values.append(arr[i][j+k])
                values.append(arr[i+2][j+k])
            values.append(arr[i+1][j+1])
            hourglass.append(values)
    for i in hourglass:
        x=sum(i)
        glass_sum.append(x)
    return max(glass_sum)
print(hourglassSum([[1,1,1,0,0,0],[1,2,3,4,5,6],[2,2,3,1,6,8],[0,0,0,0,0,0],[1,3,4,5,2,1],[2,2,4,2,6,9]]))