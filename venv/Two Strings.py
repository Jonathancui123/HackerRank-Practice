
def twoStrings(s1, s2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if (letter in s1) and (letter in s2):
            return "YES"
    return "NO"
