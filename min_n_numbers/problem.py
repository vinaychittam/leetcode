n = 3
nums = [6,1,2,3,-9,98]
def min_nums(n, nums):
    nums.sort()
    temp = []
    for i in range(n):
        temp.append(nums[i])

    return temp

print min_nums(n, nums)
