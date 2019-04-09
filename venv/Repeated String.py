#What if n is less than s?

def repeatedString(s, n):
    count = 0
    remainder = n % len(s)
    count += s[:remainder].count('a')

    if n > len(s):
        #find the number of 'a's in the repeating string
        countPerRep = s.count('a')
        #find the number of repeating strings and multiply and add to count
        count += (n // len(s))*countPerRep

    return count