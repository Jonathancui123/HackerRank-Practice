#Let n be the cloud that Emma is on
#Loop:
#Check if two clouds away (n+2) is jump-able, if it is, update cloud
#If not, jump to cloud n+1
#Increment jump count

def jumpingOnClouds(c):
    jumps = 0
    n = 0
    while n+1 < len(c):
        jumps += 1
        try:
            if c[n+2] == 0:
                n += 2
            else:
                n += 1
        except IndexError:
            n += 1
    return jumps