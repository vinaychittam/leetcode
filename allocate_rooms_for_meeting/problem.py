

pt = [9, 10, 8, 7]
et = [10.5, 11, 10, 7.5]
pt = [7,8,9,10]
et = [7.5, 10, 10.5, 11]

def get_max_rooms_allocated(pt, et):
    my_set = set()
    cnt = 0
    for ind,val  in enumerate(pt):
        if ind == 0:
            my_set.add(et[ind])
            continue
        flag = True
        for j in my_set:
            if pt[ind] >= j:
                print ("")
                my_set.remove(j)
                my_set.add(et[ind])
                flag = False
        if flag:
            cnt += 1
            my_set.add(et[ind])

    return cnt


assert 1 == get_max_rooms_allocated(pt, et)
print ("Success")
