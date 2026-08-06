nums=[1,1,2,2,3,4,5,5,5]
def removeDuplicates(nums):
    slow=1
    for fast in range(1,len(nums)):
        if nums[fast]!=nums[fast-1]:
            nums[slow]=nums[fast]
            slow+=1
    return slow

print(removeDuplicates(nums))
