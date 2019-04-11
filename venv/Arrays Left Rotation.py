def rotLeft(a, d):
    assert type(a) == list
    return a[d:]+ a[:d]

a = [1,2,3,4,5]
d = 4
print(rotLeft(a,d))