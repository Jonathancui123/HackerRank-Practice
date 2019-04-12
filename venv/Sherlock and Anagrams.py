import collections

def sherlockAndAnagrams(s):
    for subLen in range(1, len(s)):
        for i in range(len(s) - subLen):