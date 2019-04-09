#Initialize an 'altitude', 'isVal' and 'valCount' variable
#Deal with the journey in chunks above or below sea level

#Loop for each time the altitude becomes zero
#Check if the first step is up or down --> Set 'isVal'
#Increment or decrement altitude with each step
#Once altitude returns to zero, increment valCount if isVal is true



def countingValleys(n, s):
    alt = 0
    valCount = 0
    for step in s:
        if step == 'D':
            alt -= 1
        else:
            alt += 1
            if alt == 0:
                valCount += 1
    return (valCount)

