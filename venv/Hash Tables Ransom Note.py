import collections

def checkMagazine(magazine, note):
    magFreq = collections.Counter(magazine)
    noteFreq = collections.Counter(note)
    createable = True
    for word in noteFreq:
        if noteFreq[word] > magFreq[word]:
            createable = False
            break
    if createable == True:
        print("Yes")
    else:
        print("No")
