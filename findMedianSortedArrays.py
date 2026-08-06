def findMedianSortedArrays(nums1, nums2):
    arr=nums1+nums2
    arr.sort()
    i=0
    j=len(arr)-1
    if len(arr)%2!=0:
        while i<=j:
            if i==j:
                return arr[i]
            i+=1
            j-=1
    else:
        while i<j:
            if j==i+1:
                return (arr[i]+arr[j])/2
            i+=1
            j-=1


print(findMedianSortedArrays([1,2],[3,4]))