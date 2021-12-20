for i in range(len(nums)):
    minimum=i
    for j in range(i+1,len(nums)):
        if nums[j]<nums[minimum]:
            minimum=j
    nums[i],nums[minimum]=nums[minimum],nums[i]
retlst=[]
for i in range(len(nums)):
    if nums[i]==target:
        retlst.append(i)
return retlst
