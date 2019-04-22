from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        
        ind_arr = deque(range(len(deck)))
        print ind_arr
        res = []
        for i in deck:
            res.append(None)
        
        
        for item in sorted(deck):
            p_ind = ind_arr.popleft()
            res[p_ind] = item
            if len(ind_arr) > 0:
                ind_arr.append(ind_arr.popleft())

        return res
