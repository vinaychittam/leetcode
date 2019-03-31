nums = [-1, 0, -1, 2, -2]
nums1 = [-1, 0, 2, 1, 3, -3, -4, 2]
def get_max(nums):
    cnt = 0
    triplets = []
    for slow_pointer, val in enumerate(nums):
        for med_pointer, value in enumerate(nums):
            if slow_pointer >= med_pointer:
                continue
            else:
                for item in range(med_pointer, len(nums)):
                    if val + value + nums[item] == 0:
                        cnt += 1
                        temp = [val, value, nums[item]]
                        temp.sort()
                        triplets.append(tuple(temp))

    print len(set(triplets))
    return len(set(triplets))
assert 2 == get_max(nums)
assert 5 == get_max(nums1)
 
