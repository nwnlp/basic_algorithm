#填充
#[1,2]
#填充后有如下case:
#[1,1] [1,2],[2,1][2,2]
#复杂度n^n

def fill(nums,result,cur,n):
    if cur == n:#cur为填充指针，cur=n表示递归边界
        print(result)
    else:
        for i in range(n):
            result[cur] = nums[i]#对cur位置进行按序填充
            fill(nums, result, cur+1, n)#递归调用，同堆栈下对cur后面的位置进行按序填充

nums = [1,2,3]
n = len(nums)
result = [0]*n
fill(nums,result,0,n)
