def maxArea(height):
    i=0
    j=len(height)-1
    maxVol=0
    while i<j:
        if height[i]<height[j]:
            volume=(j-i)*height[i]
            i+=1
        else:
            volume=(j-i)*height[j]
            j-=1
        if maxVol<volume:
            maxVol=volume
    return maxVol
print(maxArea([1,8,6,2,5,4,8,3,7]))
            