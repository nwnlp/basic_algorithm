'''bubble sort'''
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                a = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = a
    return nums

'''selection sort'''
def selection_sort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        a = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = a
    return nums

'''insert sort'''
def insert_sort(nums, gap = 1):
    for i in range(1, len(nums)):
        j = i
        val = nums[j]
        while j>0 and val < nums[j-gap]:
            nums[j] = nums[j-gap]
            j-=gap
        nums[j] = val
    return nums

'''shell sort'''
def shell_sort(nums):
    gap = len(nums)
    while True:
        gap = int(gap/3)+1
        nums = insert_sort(nums, gap)
        if gap == 1:
            break
    return nums

'''merge sort'''
def merge(l,left,mid,right):
    i = left
    m = mid
    j = mid+1
    n = right
    t = []
    while i<=m and j<= n:
        if l[i] < l[j]:
            t.append(l[i])
            i+=1
        else:
            t.append(l[j])
            j+=1
    while i<=m:
        t.append(l[i])
        i+=1
    while j<=n:
        t.append(l[j])
        j+=1
    i = left
    k = 0
    while i<=n:
        l[i] = t[k]
        k+=1
        i+=1

def merge_sort(nums, left, right):
    if left<right:
        mid = int((left+right)/2)
        merge_sort(nums, left, mid)
        merge_sort(nums, mid+1, right)
        merge(nums, left, mid, right)

'''quick sort'''
def quick_sort(nums, left, right):
    if left < right:
        val = nums[left]
        i = left
        j = right
        while i<j:
            while j > i and nums[j]>val:
                j-=1
            if i<j:
                nums[i] = nums[j]
                i+=1
            while i < j and nums[i]<val:
                i+=1
            if i<j:
                nums[j] = nums[i]
                j-=1
        nums[i] = val
        quick_sort(nums,left,i-1)
        quick_sort(nums, i+1, right)


if __name__ == '__main__':
    nums = [6,1,2,5,9,3]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)