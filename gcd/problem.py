a = [2, 3, 4,6,8]
b = [2, 4,6,8]
c = [4,8, 12, 16]

def gcd(nums):

    mini = min(a)
    gcd = False
    while mini >= 1:
        if mini == 1:
            return 1
        gcd = True
        for num in nums:
            if num % mini == 0:
                print ("")
            else:
                gcd = False
                mini -= 1
                break
        if gcd is True:
            return mini
            
assert 1 == gcd(a)             
assert 2 == gcd(b)             
assert 2 == gcd(c)
print ("Success")             
