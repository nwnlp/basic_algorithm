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
#fill(nums,result,0,n)
"""
output:
[1, 1, 1]
[1, 1, 2]
[1, 1, 3]
[1, 2, 1]
[1, 2, 2]
[1, 2, 3]
[1, 3, 1]
[1, 3, 2]
[1, 3, 3]
[2, 1, 1]
[2, 1, 2]
[2, 1, 3]
[2, 2, 1]
[2, 2, 2]
[2, 2, 3]
[2, 3, 1]
[2, 3, 2]
[2, 3, 3]
[3, 1, 1]
[3, 1, 2]
[3, 1, 3]
[3, 2, 1]
[3, 2, 2]
[3, 2, 3]
[3, 3, 1]
[3, 3, 2]
[3, 3, 3]
"""

#循环方式写出排列形式，循环嵌套层数是n
def permutation1(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i] == nums[j]:
                continue
            for k in range(n):
                if nums[k] == nums[i] or nums[k] == nums[j]:
                    continue
                print(nums[i],nums[j],nums[k])
"""
output:
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""
#permutation1(nums)

#排列，按字典顺序输出
#和填充的求解方法类似，排除了元素重复的情况
def permutation2(nums, result, cur, n):
    if cur == n:
        print(result)
    else:
        for num in nums:
            ok = 1
            for k in range(cur):
                if result[k] == num:
                    ok = 0
                    break
            if ok:
                result[cur] = num
                permutation2(nums,result,cur+1,n)
"""
output
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
"""
result = [0]*n
permutation2(nums,result,0,n)

#permutation2对输入是[1,1,1]的情况没有解答
#permutation3利用c1统计当前num已出现的次数，c2统计num一共的次数，c1<c2表示num还能够使用

def permutation3(nums, result, cur, n):
    if cur == n:
        print(result)
    else:
        for i, num in enumerate(nums):
            if(i and num == nums[i-1]):#避免重复，保证cur位置的元素与cur-1的位置元素不重复(nums数组必须保证有序)
                continue
            c1,c2=0,0
            for k in range(cur):
                if result[k] == num:
                    c1+=1
            for k in range(n):
                if nums[k] == num:
                    c2+=1
            if c1 < c2:
                result[cur] = num
                permutation3(nums,result,cur+1,n)

result = [0]*n
permutation3(nums,result,0,n)