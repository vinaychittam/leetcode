nums = [-1, 0, -1, 2, -2]
nums1 = [-1, 0, 2, 1, 3, -3, -4, 2]
def get_max(nums):
    cnt = 0
    triplets = []
    seen = {}
    for i in nums:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    for slow_pointer, val in enumerate(nums):
        for med_pointer, value in enumerate(nums):
            if slow_pointer >= med_pointer:
                continue
            else:
                import pdb; pdb.set_trace()
                if -(val + value) in seen.keys() and seen[-(val + value)] > 0 :
                    #if seen[-(val + value)] > 0:
                    temp = -(val + value)
                    import pdb; pdb.set_trace()
                    cnt += 1
                    print seen
                    seen[-(val+value)] = seen[-(val+value)] - 1
                    print seen

    print cnt
    print len(seen)
    print cnt
    return cnt
get_max(nums)
#assert 2 == get_max(nums)
#import pdb; pdb.set_trace()
#print a
#assert 5 == get_max(nums1)
