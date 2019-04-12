#INCORRECT, UNSOLVED
def minimumBribes(q):
    swap = 0
    for num in q:
        if (num - 1) > q.index(num):
            diff = (num - 1) - q.index(num)
            if diff == 1 or diff == 2:
                swap += diff
            else:
                return("Too chaotic")
    return (swap)
q = [2,1,5,3,4]
print(minimumBribes(q))
