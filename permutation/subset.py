
#增量构造输入子集合
def print_subset(nums, result, cur):
    if cur>0:
        print(result[:cur])
    if cur == len(nums):#递归边界
        return
    for num in nums:
        c1,c2 = 0,0
        if cur and result[cur-1]>num:#保证"前面"的元素比"后面"小，避免输出[2，1]这样的case
            continue
        for k in range(cur):
            if result[k] == num:
                c1+=1
        for k in range(len(nums)):
            if nums[k] == num:
                c2+=1
        if c1<c2:
            result[cur] = num
            print_subset(nums, result, cur+1)


nums = [1,2,3]
result = [0]*len(nums)
print_subset(nums, result, 0)
"""
output:
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
"""