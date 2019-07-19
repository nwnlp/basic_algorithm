#最大连续和
#O(n^2)
def maxsum1(nums):
    #s表示前缀和
    #s_0 = 0
    #s_1 = a_0
    #s_2 = a_0+a_1
    #...
    #s_n+1 = a_0+a_1+...a_n
    #s_n+1 = s_n+a_n
    #s_3-s_1 = a_1+a_2
    s = [0]*(len(nums)+1)
    for i, num in enumerate(nums):
        s[i+1] = s[i]+num
    res = -100000
    for i in range(1, len(s)):
        for j in range(0, i):
            res = max(res, s[i]-s[j])
    return res

#O(n)
def maxsum2(nums):
    #s_j-s_i表示sum(a_i...a_j-1)
    #固定住s_j选取s_i最小的，差就最大
    s = [0] * (len(nums) + 1)
    s_min = 100000
    res = -100000
    for i, num in enumerate(nums):
        s[i + 1] = s[i] + num
        s_min = min(s_min, s[i])
        res = max(res, s[i+1]-s_min)
    return res

#分治法O(nlogn)
#划分问题：把数组等分切成两半 [x,y)->[x,mid)+[mid,y) mid = x+(y-x)/2
#递归求解：对子问题[x,mid)，[mid,y)递归求解
#合并问题：问题的解有三种可能，出现在左边，出现在右边，出现在中间
def maxsum3(nums, x, y):
    if y-x == 1:
        return nums[x]
    mid = x+(y-x)//2
    L = maxsum3(nums, x, mid)
    R = maxsum3(nums, mid, y)
    M = -100000
    tmp1 = 0
    for i in range(mid-1, x-1, -1):
        tmp1 += nums[i]
        M = max(M, tmp1)
    N = -100000
    tmp2 = 0
    for j in range(mid, y):
        tmp2 += nums[j]
        N = max(N, tmp2)
    return max(L,R,M+N)

nums = [1,2,4,5,-56]
res = maxsum3(nums, 0, len(nums))

print(res)