import collections
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def sherlockAndAnagrams(s):
    pairs = 0
    for subLen in range(1, len(s)):
        #Loop through each possible substring length and initialize a list for counters at this length
        nameList = []
        for i in range(len(s) - subLen + 1):
            newCounter = collections.Counter(s[i:(i+subLen)])
            print(newCounter)
            newName = str((sorted(newCounter))) + str(sorted(newCounter.items()))
            nameList.append(newName)

        dupDict = collections.Counter(nameList)
        print(dupDict)
        for num in dupDict.values():
            if num > 1:
                pairs += int(ncr(num,2))
    return pairs