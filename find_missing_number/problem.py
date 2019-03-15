

nums0 = [0,2,3,4,5]
nums1 = [0,1, 2,3,4,5]
nums2 = [1, 2,3,4,5]
def find_missing_number(nums):
    my_set = set(nums)
    if 0 not in my_set:
        return 0
    for ind, num in enumerate(nums):
        if ind == len(nums) - 1:
            return num + 1
        if num + 1 not  in my_set:
            return num + 1

assert 1 == find_missing_number(nums0)
assert 6 == find_missing_number(nums1)
assert 0 == find_missing_number(nums2)
print ("Success")
        
    
